"""
Functions generators: domain, range, inverse, composite
"""
import random
from sympy import symbols, sqrt
from generators.base import QuestionGenerator, QuestionResult

x = symbols('x')


class FunctionsDomainRangeGenerator(QuestionGenerator):
    def generate(self) -> dict:
        func_type = random.choice(['linear', 'rational', 'sqrt'])
        
        if func_type == 'linear':
            a = random.randint(1, 5)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            val = a * c + b
            
            return QuestionResult(
                question=f"إذا كانت f(x) = {a}x + {b}، أوجد f({c}):",
                expression="",
                answer=str(val),
                hints=[f"f({c}) = {a}({c}) + {b} = {val}"],
                skill_id="functions-domain-range",
                difficulty=self.difficulty
            ).to_dict()
        
        elif func_type == 'rational':
            a = random.randint(1, 5)
            
            return QuestionResult(
                question="ما مجال الدالة:",
                expression=f"f(x) = \\frac{{1}}{{x - {a}}}",
                answer=f"x ≠ {a}",
                hints=["المقام لا يمكن أن يساوي صفراً"],
                skill_id="functions-domain-range",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # sqrt
            a = random.randint(1, 10)
            
            return QuestionResult(
                question="ما مجال الدالة:",
                expression=f"f(x) = \\sqrt{{x - {a}}}",
                answer=f"x >= {a}",
                hints=["ما تحت الجذر يجب أن يكون ≥ 0"],
                skill_id="functions-domain-range",
                difficulty=self.difficulty
            ).to_dict()


class InverseCompositeFunctionsGenerator(QuestionGenerator):
    def generate(self) -> dict:
        func_type = random.choice(['composite', 'inverse'])
        
        if func_type == 'composite':
            a = random.randint(1, 3)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            
            # f(x) = ax + b, g(x) = x + c, find f(g(2))
            g_val = 2 + c
            f_g_val = a * g_val + b
            
            return QuestionResult(
                question=f"إذا كانت f(x) = {a}x + {b} و g(x) = x + {c}، أوجد f(g(2)):",
                expression="",
                answer=str(f_g_val),
                hints=[f"g(2) = {g_val}، f({g_val}) = {f_g_val}"],
                skill_id="inverse-composite-functions",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # inverse
            a = random.randint(2, 5)
            b = random.randint(1, 10)
            
            return QuestionResult(
                question="أوجد الدالة العكسية:",
                expression=f"f(x) = {a}x + {b}",
                answer=f"f^{{-1}}(x) = (x - {b})/{a}",
                hints=[f"y = {a}x + {b} → x = (y - {b})/{a}"],
                skill_id="inverse-composite-functions",
                difficulty=self.difficulty
            ).to_dict()


class LogarithmsGenerator(QuestionGenerator):
    def generate(self) -> dict:
        log_type = random.choice(['basic', 'property', 'solve'])
        
        if log_type == 'basic':
            base = random.choice([2, 3, 5, 10])
            exp = random.randint(2, 4)
            val = base ** exp
            
            return QuestionResult(
                question="احسب:",
                expression=f"\\log_{{{base}}} {val}",
                answer=str(exp),
                hints=[f"{base}^{exp} = {val}"],
                skill_id="logarithms",
                difficulty=self.difficulty
            ).to_dict()
        
        elif log_type == 'property':
            base = random.randint(2, 5)
            exp = random.randint(2, 5)
            
            return QuestionResult(
                question="بسّط:",
                expression=f"\\log_{{{base}}} {base}^{exp}",
                answer=str(exp),
                hints=["log_a(a^n) = n"],
                skill_id="logarithms",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # solve
            base = random.choice([2, 3, 5])
            exp = random.randint(2, 4)
            val = base ** exp
            
            return QuestionResult(
                question="حل المعادلة:",
                expression=f"\\log_{{{base}}} x = {exp}",
                answer=str(val),
                hints=[f"x = {base}^{exp} = {val}"],
                skill_id="logarithms",
                difficulty=self.difficulty
            ).to_dict()


class ComplexNumbersGenerator(QuestionGenerator):
    def generate(self) -> dict:
        op_type = random.choice(['simplify', 'add', 'multiply'])
        
        if op_type == 'simplify':
            n = random.choice([4, 9, 16, 25, 36])
            
            return QuestionResult(
                question="بسّط:",
                expression=f"\\sqrt{{-{n}}}",
                answer=f"{int(n**0.5)}i",
                hints=[f"√(-{n}) = √{n} × √(-1) = {int(n**0.5)}i"],
                skill_id="complex-numbers",
                difficulty=self.difficulty
            ).to_dict()
        
        elif op_type == 'add':
            a, b = random.randint(1, 5), random.randint(1, 5)
            c, d = random.randint(1, 5), random.randint(-5, 5)
            
            real = a + c
            imag = b + d
            
            return QuestionResult(
                question="احسب:",
                expression=f"({a} + {b}i) + ({c} {'+' if d >= 0 else ''} {d}i)",
                answer=f"{real} {'+' if imag >= 0 else ''} {imag}i",
                hints=["اجمع الأجزاء الحقيقية والتخيلية منفصلة"],
                skill_id="complex-numbers",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # multiply
            return QuestionResult(
                question="احسب:",
                expression="i^2",
                answer="-1",
                hints=["i² = -1 بالتعريف"],
                skill_id="complex-numbers",
                difficulty=self.difficulty
            ).to_dict()
