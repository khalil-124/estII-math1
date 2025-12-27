"""
Fraction and ratio generators
"""
import random
from math import gcd
from generators.base import QuestionGenerator, QuestionResult

class FractionsGenerator(QuestionGenerator):
    """Generate fraction operations"""
    
    def generate(self) -> dict:
        operation = random.choice(['add', 'sub', 'mul', 'div'])
        
        # Generate fractions with reasonable denominators
        denoms = [2, 3, 4, 5, 6, 8, 10, 12]
        d1 = random.choice(denoms[:4] if self.difficulty <= 2 else denoms)
        d2 = random.choice(denoms[:4] if self.difficulty <= 2 else denoms)
        n1 = random.randint(1, d1 - 1)
        n2 = random.randint(1, d2 - 1)
        
        if operation == 'add':
            # Find LCD and add
            lcd = (d1 * d2) // gcd(d1, d2)
            result_num = n1 * (lcd // d1) + n2 * (lcd // d2)
            result_den = lcd
            expr = f"\\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}}"
            hint = f"وحّد المقامات أولاً: LCD = {lcd}"
        elif operation == 'sub':
            # Ensure positive result
            f1 = n1 / d1
            f2 = n2 / d2
            if f2 > f1:
                n1, n2 = n2, n1
                d1, d2 = d2, d1
            lcd = (d1 * d2) // gcd(d1, d2)
            result_num = n1 * (lcd // d1) - n2 * (lcd // d2)
            result_den = lcd
            expr = f"\\frac{{{n1}}}{{{d1}}} - \\frac{{{n2}}}{{{d2}}}"
            hint = f"وحّد المقامات أولاً: LCD = {lcd}"
        elif operation == 'mul':
            result_num = n1 * n2
            result_den = d1 * d2
            expr = f"\\frac{{{n1}}}{{{d1}}} \\times \\frac{{{n2}}}{{{d2}}}"
            hint = "اضرب البسوط معاً والمقامات معاً"
        else:  # div
            result_num = n1 * d2
            result_den = d1 * n2
            expr = f"\\frac{{{n1}}}{{{d1}}} \\div \\frac{{{n2}}}{{{d2}}}"
            hint = "القسمة = الضرب في المقلوب"
        
        # Simplify result
        g = gcd(abs(result_num), abs(result_den))
        result_num //= g
        result_den //= g
        
        if result_den == 1:
            answer = str(result_num)
        else:
            answer = f"{result_num}/{result_den}"
        
        return QuestionResult(
            question="احسب:",
            expression=expr,
            answer=answer,
            hints=[hint],
            skill_id="fractions",
            difficulty=self.difficulty
        ).to_dict()


class RatiosGenerator(QuestionGenerator):
    """Generate ratio and proportion questions"""
    
    def generate(self) -> dict:
        question_type = random.choice(['simplify', 'proportion', 'percent'])
        
        if question_type == 'simplify':
            # Simplify a ratio
            g = random.randint(2, 6)
            a = random.randint(1, 10) * g
            b = random.randint(1, 10) * g
            
            g_common = gcd(a, b)
            answer = f"{a // g_common}:{b // g_common}"
            
            return QuestionResult(
                question="بسّط النسبة:",
                expression=f"{a}:{b}",
                answer=answer,
                hints=[f"اقسم كلا الطرفين على {g_common}"],
                skill_id="ratios",
                difficulty=self.difficulty
            ).to_dict()
        
        elif question_type == 'proportion':
            # Solve proportion a:b = c:x
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = a * random.randint(2, 5)
            x = (b * c) // a
            
            return QuestionResult(
                question=f"إذا كانت النسبة {a}:{b}، وكان العدد الأول {c}، فما العدد الثاني؟",
                expression="",
                answer=str(x),
                hints=[f"{a}/{b} = {c}/x، إذن x = {b} × {c} ÷ {a}"],
                skill_id="ratios",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # percent
            # Convert fraction to percent
            denoms = [2, 4, 5, 10, 20, 25]
            d = random.choice(denoms)
            n = random.randint(1, d)
            percent = int((n / d) * 100)
            
            return QuestionResult(
                question="حوّل إلى نسبة مئوية:",
                expression=f"\\frac{{{n}}}{{{d}}}",
                answer=f"{percent}%",
                hints=[f"{n}/{d} = {n/d} = {percent}%"],
                skill_id="ratios",
                difficulty=self.difficulty
            ).to_dict()


class PrimeFactorizationGenerator(QuestionGenerator):
    """Generate prime factorization, GCF, LCM questions"""
    
    def generate(self) -> dict:
        question_type = random.choice(['factor', 'gcf', 'lcm'])
        
        if question_type == 'factor':
            # Generate a number to factorize
            primes = [2, 3, 5, 7, 11]
            num_primes = 2 if self.difficulty <= 2 else 3
            factors = random.choices(primes[:3 if self.difficulty <= 3 else 5], k=num_primes)
            n = 1
            for f in factors:
                n *= f
            
            # Build answer
            from collections import Counter
            counts = Counter(factors)
            answer_parts = []
            for p, c in sorted(counts.items()):
                if c == 1:
                    answer_parts.append(str(p))
                else:
                    answer_parts.append(f"{p}^{c}")
            answer = " × ".join(answer_parts)
            
            return QuestionResult(
                question="حلل العدد إلى عوامله الأولية:",
                expression=str(n),
                answer=answer,
                hints=["ابدأ بالقسمة على أصغر عدد أولي"],
                skill_id="prime-factorization",
                difficulty=self.difficulty
            ).to_dict()
        
        elif question_type == 'gcf':
            # Generate two numbers and find GCF
            base = random.randint(2, 8)
            a = base * random.randint(2, 6)
            b = base * random.randint(2, 6)
            g = gcd(a, b)
            
            return QuestionResult(
                question="أوجد العامل المشترك الأكبر (GCF):",
                expression=f"\\gcd({a}, {b})",
                answer=str(g),
                hints=[f"حلل {a} و {b} إلى عوامل أولية"],
                skill_id="prime-factorization",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # lcm
            a = random.randint(3, 12)
            b = random.randint(3, 12)
            lcm = (a * b) // gcd(a, b)
            
            return QuestionResult(
                question="أوجد المضاعف المشترك الأصغر (LCM):",
                expression=f"\\text{{lcm}}({a}, {b})",
                answer=str(lcm),
                hints=[f"LCM = ({a} × {b}) ÷ GCF({a}, {b})"],
                skill_id="prime-factorization",
                difficulty=self.difficulty
            ).to_dict()
