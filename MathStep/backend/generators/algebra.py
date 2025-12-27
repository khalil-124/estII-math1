"""
Algebra generators: equations, inequalities, systems
"""
import random
from sympy import symbols, Eq, solve, expand, simplify, latex
from generators.base import QuestionGenerator, QuestionResult

x = symbols('x')
y = symbols('y')


class LinearEquationsGenerator(QuestionGenerator):
    """Generate linear equations"""
    
    def generate(self) -> dict:
        complexity = self.difficulty
        
        if complexity <= 2:
            # Simple: ax + b = c
            a = random.randint(1, 5)
            solution = random.randint(1, 10)
            b = random.randint(1, 10)
            c = a * solution + b
            
            expr = f"{a}x + {b} = {c}"
            hint = f"اطرح {b} من الطرفين، ثم اقسم على {a}"
        
        elif complexity == 3:
            # Medium: ax + b = cx + d
            a = random.randint(2, 6)
            c = random.randint(1, a - 1)  # Ensure a > c
            solution = random.randint(1, 10)
            b = random.randint(1, 10)
            d = (a - c) * solution + b
            
            expr = f"{a}x + {b} = {c}x + {d}"
            hint = "اجمع المتغيرات في طرف والأرقام في طرف آخر"
        
        else:
            # Hard: a(x + b) = c(x + d)
            a = random.randint(2, 5)
            c = random.randint(2, 5)
            b = random.randint(1, 5)
            d = random.randint(1, 5)
            
            # Solve symbolically
            eq = Eq(a * (x + b), c * (x + d))
            solution = solve(eq, x)[0]
            
            expr = f"{a}(x + {b}) = {c}(x + {d})"
            hint = "فك الأقواس أولاً، ثم اجمع الحدود المتشابهة"
        
        # Re-solve to get the answer
        if complexity <= 3:
            solution = solution if 'solution' in dir() else (c - b) // a
        
        return QuestionResult(
            question="حل المعادلة:",
            expression=expr,
            answer=str(solution),
            hints=[hint],
            skill_id="linear-equations",
            difficulty=self.difficulty
        ).to_dict()


class InequalitiesGenerator(QuestionGenerator):
    """Generate linear inequalities"""
    
    def generate(self) -> dict:
        a = random.randint(2, 8)
        b = random.randint(1, 15)
        c = random.randint(10, 30)
        
        # Random inequality type
        ineq_type = random.choice(['>', '<', '>=', '<='])
        
        if self.difficulty <= 2:
            # Simple: ax + b > c (positive coefficient)
            expr = f"{a}x + {b} {ineq_type.replace('>=', '\\geq').replace('<=', '\\leq')} {c}"
            solution_val = (c - b) / a
            
            if ineq_type in ['>', '>=']:
                answer = f"x {'>' if ineq_type == '>' else '≥'} {solution_val:.0f}" if solution_val == int(solution_val) else f"x {'>' if ineq_type == '>' else '≥'} {solution_val}"
            else:
                answer = f"x {'<' if ineq_type == '<' else '≤'} {solution_val:.0f}" if solution_val == int(solution_val) else f"x {'<' if ineq_type == '<' else '≤'} {solution_val}"
            
            hint = f"اطرح {b}، ثم اقسم على {a}"
        
        else:
            # Hard: -ax + b > c (negative coefficient - flip inequality)
            a = -abs(a)
            expr = f"{a}x + {b} {ineq_type.replace('>=', '\\geq').replace('<=', '\\leq')} {c}"
            solution_val = (c - b) / a
            
            # Flip inequality for negative division
            flipped = {'<': '>', '>': '<', '<=': '>=', '>=': '<='}
            flipped_type = flipped[ineq_type]
            
            if flipped_type in ['>', '>=']:
                answer = f"x {'>' if flipped_type == '>' else '≥'} {solution_val:.0f}" if solution_val == int(solution_val) else f"x {'>' if flipped_type == '>' else '≥'} {solution_val}"
            else:
                answer = f"x {'<' if flipped_type == '<' else '≤'} {solution_val:.0f}" if solution_val == int(solution_val) else f"x {'<' if flipped_type == '<' else '≤'} {solution_val}"
            
            hint = "عند القسمة على سالب، اعكس إشارة المتباينة"
        
        return QuestionResult(
            question="حل المتباينة:",
            expression=expr,
            answer=answer,
            hints=[hint],
            skill_id="inequalities",
            difficulty=self.difficulty
        ).to_dict()


class DistributivePropertyGenerator(QuestionGenerator):
    """Generate distributive property questions"""
    
    def generate(self) -> dict:
        if self.difficulty <= 2:
            # Single distribution: a(x + b)
            a = random.randint(2, 6) * random.choice([1, -1])
            b = random.randint(1, 10) * random.choice([1, -1])
            
            result = expand(a * (x + b))
            expr = f"{a}(x {'+' if b > 0 else ''} {b})"
            answer = str(result).replace('**', '^').replace('*', '')
            hint = f"وزّع {a} على كل حد داخل الأقواس"
        
        else:
            # Double distribution: a(x + b) + c(x + d)
            a = random.randint(2, 5)
            b = random.randint(1, 5)
            c = random.randint(2, 5)
            d = random.randint(1, 5) * random.choice([1, -1])
            
            result = expand(a * (x + b) + c * (x + d))
            expr = f"{a}(x + {b}) + {c}(x {'+' if d > 0 else ''} {d})"
            answer = str(result).replace('**', '^').replace('*', '')
            hint = "فك كل قوس على حدة، ثم اجمع الحدود المتشابهة"
        
        return QuestionResult(
            question="فك الأقواس وبسّط:",
            expression=expr,
            answer=answer,
            hints=[hint],
            skill_id="distributive-property",
            difficulty=self.difficulty
        ).to_dict()


class ExponentsGenerator(QuestionGenerator):
    """Generate exponent questions"""
    
    def generate(self) -> dict:
        question_type = random.choice(['power', 'multiply', 'divide', 'power_of_power'])
        
        if question_type == 'power':
            base = random.randint(2, 5)
            exp = random.randint(2, 4 if self.difficulty <= 2 else 6)
            answer = base ** exp
            
            return QuestionResult(
                question="احسب:",
                expression=f"{base}^{exp}",
                answer=str(answer),
                hints=[f"{base}^{exp} = {' × '.join([str(base)] * exp)}"],
                skill_id="exponents",
                difficulty=self.difficulty
            ).to_dict()
        
        elif question_type == 'multiply':
            # x^a * x^b = x^(a+b)
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            
            return QuestionResult(
                question="بسّط:",
                expression=f"x^{a} \\cdot x^{b}",
                answer=f"x^{a + b}",
                hints=["عند ضرب أسس لها نفس القاعدة، اجمع الأسس"],
                skill_id="exponents",
                difficulty=self.difficulty
            ).to_dict()
        
        elif question_type == 'divide':
            # x^a / x^b = x^(a-b)
            a = random.randint(4, 8)
            b = random.randint(1, a - 1)
            
            return QuestionResult(
                question="بسّط:",
                expression=f"\\frac{{x^{a}}}{{x^{b}}}",
                answer=f"x^{a - b}",
                hints=["عند قسمة أسس لها نفس القاعدة، اطرح الأسس"],
                skill_id="exponents",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # power_of_power
            # (x^a)^b = x^(a*b)
            a = random.randint(2, 4)
            b = random.randint(2, 3)
            
            return QuestionResult(
                question="بسّط:",
                expression=f"(x^{a})^{b}",
                answer=f"x^{a * b}",
                hints=["أس الأس = ضرب الأسس"],
                skill_id="exponents",
                difficulty=self.difficulty
            ).to_dict()


class SystemsOfEquationsGenerator(QuestionGenerator):
    """Generate systems of linear equations"""
    
    def generate(self) -> dict:
        # Generate solution first
        sol_x = random.randint(1, 8)
        sol_y = random.randint(1, 8)
        
        # Generate coefficients
        a1 = random.randint(1, 4)
        b1 = random.randint(1, 4)
        c1 = a1 * sol_x + b1 * sol_y
        
        a2 = random.randint(1, 4)
        b2 = random.randint(1, 4)
        # Make sure equations are not parallel
        while a1 * b2 == a2 * b1:
            a2 = random.randint(1, 4)
            b2 = random.randint(1, 4)
        c2 = a2 * sol_x + b2 * sol_y
        
        expr = f"{a1}x + {b1}y = {c1} \\\\ {a2}x + {b2}y = {c2}"
        
        # Randomly ask for x or y
        if random.choice([True, False]):
            answer = str(sol_x)
            question = "حل النظام (أوجد x):"
        else:
            answer = str(sol_y)
            question = "حل النظام (أوجد y):"
        
        return QuestionResult(
            question=question,
            expression=expr,
            answer=answer,
            hints=["استخدم طريقة التعويض أو الحذف"],
            skill_id="systems-of-equations",
            difficulty=self.difficulty
        ).to_dict()


class SlopeLineEquationsGenerator(QuestionGenerator):
    """Generate slope and line equation questions"""
    
    def generate(self) -> dict:
        question_type = random.choice(['find_slope', 'write_equation', 'from_points'])
        
        if question_type == 'find_slope':
            m = random.randint(-5, 5)
            if m == 0:
                m = 2
            b = random.randint(-10, 10)
            
            return QuestionResult(
                question="ما ميل الخط:",
                expression=f"y = {m}x {'+' if b >= 0 else ''} {b}",
                answer=str(m),
                hints=["في صيغة y = mx + b، الميل هو m"],
                skill_id="slope-line-equations",
                difficulty=self.difficulty
            ).to_dict()
        
        elif question_type == 'write_equation':
            m = random.randint(1, 5) * random.choice([1, -1])
            x1 = random.randint(1, 5)
            y1 = random.randint(1, 10)
            b = y1 - m * x1
            
            return QuestionResult(
                question=f"اكتب معادلة الخط بميل {m} ويمر بالنقطة ({x1}, {y1}):",
                expression="",
                answer=f"y = {m}x {'+' if b >= 0 else ''} {b}",
                hints=[f"استخدم y - {y1} = {m}(x - {x1})"],
                skill_id="slope-line-equations",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # from_points
            x1 = random.randint(0, 5)
            y1 = random.randint(0, 10)
            x2 = x1 + random.randint(1, 5)
            y2 = y1 + random.randint(-5, 5)
            
            m = (y2 - y1) / (x2 - x1) if x2 != x1 else 0
            
            return QuestionResult(
                question="أوجد ميل الخط المار بالنقطتين:",
                expression=f"({x1}, {y1}) \\text{{ و }} ({x2}, {y2})",
                answer=str(int(m) if m == int(m) else round(m, 2)),
                hints=[f"m = (y₂ - y₁) / (x₂ - x₁) = ({y2} - {y1}) / ({x2} - {x1})"],
                skill_id="slope-line-equations",
                difficulty=self.difficulty
            ).to_dict()
