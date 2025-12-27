"""
Calculus generators: derivatives, integrals, limits
"""
import random
from sympy import symbols, diff, integrate, limit, oo, sin, cos, exp, log, latex
from generators.base import QuestionGenerator, QuestionResult

x = symbols('x')


class LimitsContinuityGenerator(QuestionGenerator):
    def generate(self) -> dict:
        limit_type = random.choice(['direct', 'factor', 'infinity'])
        
        if limit_type == 'direct':
            a = random.randint(1, 5)
            b = random.randint(1, 10)
            c = random.randint(1, 5)
            val = a*c + b
            
            return QuestionResult(
                question="أوجد النهاية:",
                expression=f"\\lim_{{x \\to {c}}} ({a}x + {b})",
                answer=str(val),
                hints=["عوّض مباشرة"],
                skill_id="limits-continuity",
                difficulty=self.difficulty
            ).to_dict()
        
        elif limit_type == 'factor':
            a = random.randint(2, 5)
            expr = f"\\lim_{{x \\to {a}}} \\frac{{x^2 - {a**2}}}{{x - {a}}}"
            answer = 2 * a
            
            return QuestionResult(
                question="أوجد النهاية:",
                expression=expr,
                answer=str(answer),
                hints=[f"حلل البسط: x² - {a**2} = (x+{a})(x-{a})"],
                skill_id="limits-continuity",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # infinity
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            
            return QuestionResult(
                question="أوجد النهاية:",
                expression=f"\\lim_{{x \\to \\infty}} \\frac{{{a}x^2 + 1}}{{{b}x^2 - 3}}",
                answer=f"{a}/{b}" if a != b else "1",
                hints=["اقسم على أعلى قوة"],
                skill_id="limits-continuity",
                difficulty=self.difficulty
            ).to_dict()


class DerivativesRulesGenerator(QuestionGenerator):
    def generate(self) -> dict:
        deriv_type = random.choice(['power', 'sum', 'product'])
        
        if deriv_type == 'power':
            n = random.randint(2, 6)
            a = random.randint(1, 5)
            f = a * x**n
            df = diff(f, x)
            
            return QuestionResult(
                question="اشتق:",
                expression=f"f(x) = {a}x^{n}",
                answer=f"{a*n}x^{n-1}",
                hints=["قاعدة القوة: d/dx(xⁿ) = nxⁿ⁻¹"],
                skill_id="derivatives-rules",
                difficulty=self.difficulty
            ).to_dict()
        
        elif deriv_type == 'sum':
            a = random.randint(1, 5)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            
            return QuestionResult(
                question="اشتق:",
                expression=f"f(x) = {a}x^2 + {b}x - {c}",
                answer=f"{2*a}x + {b}",
                hints=["اشتق كل حد على حدة"],
                skill_id="derivatives-rules",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # product hint
            return QuestionResult(
                question="اشتق:",
                expression="f(x) = x \\cdot e^x",
                answer="e^x + x \\cdot e^x",
                hints=["قاعدة الضرب: (uv)' = u'v + uv'"],
                skill_id="derivatives-rules",
                difficulty=self.difficulty
            ).to_dict()


class ChainRuleGenerator(QuestionGenerator):
    def generate(self) -> dict:
        chain_type = random.choice(['power', 'exp', 'trig'])
        
        if chain_type == 'power':
            a = random.randint(2, 5)
            b = random.randint(1, 5)
            n = random.randint(2, 4)
            
            return QuestionResult(
                question="اشتق:",
                expression=f"f(x) = ({a}x + {b})^{n}",
                answer=f"{n*a}({a}x + {b})^{n-1}",
                hints=["قاعدة السلسلة: اشتق الخارج × مشتقة الداخل"],
                skill_id="chain-rule",
                difficulty=self.difficulty
            ).to_dict()
        
        elif chain_type == 'exp':
            a = random.randint(2, 4)
            
            return QuestionResult(
                question="اشتق:",
                expression=f"f(x) = e^{{{a}x}}",
                answer=f"{a}e^{{{a}x}}",
                hints=["d/dx(e^u) = e^u × u'"],
                skill_id="chain-rule",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # trig
            return QuestionResult(
                question="اشتق:",
                expression="f(x) = \\sin(x^2)",
                answer="2x \\cos(x^2)",
                hints=["d/dx(sin(u)) = cos(u) × u'"],
                skill_id="chain-rule",
                difficulty=self.difficulty
            ).to_dict()


class IntegralsGenerator(QuestionGenerator):
    def generate(self) -> dict:
        int_type = random.choice(['power', 'definite', 'exp'])
        
        if int_type == 'power':
            n = random.randint(1, 4)
            a = random.randint(1, 5)
            
            return QuestionResult(
                question="احسب التكامل:",
                expression=f"\\int {a}x^{n} \\, dx",
                answer=f"\\frac{{{a}}}{{ {n+1} }}x^{n+1} + C",
                hints=["∫xⁿ dx = xⁿ⁺¹/(n+1) + C"],
                skill_id="integrals",
                difficulty=self.difficulty
            ).to_dict()
        
        elif int_type == 'definite':
            a = random.randint(0, 2)
            b = random.randint(3, 5)
            # ∫x dx from a to b = b²/2 - a²/2
            answer = (b**2 - a**2) // 2
            
            return QuestionResult(
                question="احسب التكامل المحدود:",
                expression=f"\\int_{{{a}}}^{{{b}}} x \\, dx",
                answer=str(answer),
                hints=[f"[x²/2]_{a}^{b} = {b}²/2 - {a}²/2"],
                skill_id="integrals",
                difficulty=self.difficulty
            ).to_dict()
        
        else:  # exp
            return QuestionResult(
                question="احسب التكامل:",
                expression="\\int e^x \\, dx",
                answer="e^x + C",
                hints=["∫eˣ dx = eˣ + C"],
                skill_id="integrals",
                difficulty=self.difficulty
            ).to_dict()


class UnitCircleGenerator(QuestionGenerator):
    def generate(self) -> dict:
        angles = [
            (0, "0", "1", "0"),
            (30, "\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "\\frac{1}{\\sqrt{3}}"),
            (45, "\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{2}}{2}", "1"),
            (60, "\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}", "\\sqrt{3}"),
            (90, "1", "0", "undefined"),
        ]
        
        angle, sin_val, cos_val, tan_val = random.choice(angles)
        func = random.choice(['sin', 'cos', 'tan'])
        
        if func == 'sin':
            answer = sin_val
            expr = f"\\sin({angle}°)"
        elif func == 'cos':
            answer = cos_val
            expr = f"\\cos({angle}°)"
        else:
            answer = tan_val
            expr = f"\\tan({angle}°)"
        
        return QuestionResult(
            question="احسب:",
            expression=expr,
            answer=answer,
            hints=["راجع قيم دائرة الوحدة"],
            skill_id="unit-circle",
            difficulty=self.difficulty
        ).to_dict()
