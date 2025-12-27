"""
Polynomial and factoring generators
"""
import random
from sympy import symbols, expand, factor
from generators.base import QuestionGenerator, QuestionResult

x = symbols('x')


class PolynomialsGenerator(QuestionGenerator):
    def generate(self) -> dict:
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5) * random.choice([1, -1])
        
        result = expand(a * x * (x + c))
        
        return QuestionResult(
            question="اضرب:",
            expression=f"{a}x(x {'+' if c >= 0 else ''} {c})",
            answer=str(result).replace('**', '^').replace('*', ''),
            hints=["وزّع على كل حد داخل الأقواس"],
            skill_id="polynomials",
            difficulty=self.difficulty
        ).to_dict()


class FactoringGenerator(QuestionGenerator):
    def generate(self) -> dict:
        r = random.randint(1, 6) * random.choice([1, -1])
        s = random.randint(1, 6) * random.choice([1, -1])
        
        expr = expand((x + r) * (x + s))
        factored = factor(expr)
        
        return QuestionResult(
            question="حلل:",
            expression=str(expr).replace('**', '^').replace('*', ''),
            answer=str(factored),
            hints=[f"ابحث عن عددين حاصل ضربهما {r*s} ومجموعهما {r+s}"],
            skill_id="factoring",
            difficulty=self.difficulty
        ).to_dict()


class QuadraticEquationsGenerator(QuestionGenerator):
    def generate(self) -> dict:
        r1 = random.randint(1, 6) * random.choice([1, -1])
        r2 = random.randint(1, 6) * random.choice([1, -1])
        
        b = -(r1 + r2)
        c = r1 * r2
        
        expr = f"x^2 {'+' if b >= 0 else ''} {b}x {'+' if c >= 0 else ''} {c} = 0"
        
        return QuestionResult(
            question="حل بالتحليل:",
            expression=expr,
            answer=f"x = {r1}, {r2}",
            hints=[f"ابحث عن عددين حاصل ضربهما {c} ومجموعهما {-b}"],
            skill_id="quadratic-equations",
            difficulty=self.difficulty
        ).to_dict()


class PythagoreanTheoremGenerator(QuestionGenerator):
    def generate(self) -> dict:
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
        a, b, c = random.choice(triples)
        
        return QuestionResult(
            question=f"في مثلث قائم، الضلعان {a} و {b}، ما الوتر؟",
            expression="",
            answer=str(c),
            hints=[f"c² = {a}² + {b}² = {a**2 + b**2}"],
            skill_id="pythagorean-theorem",
            difficulty=self.difficulty
        ).to_dict()


class SimilarityGenerator(QuestionGenerator):
    def generate(self) -> dict:
        ratio = random.randint(2, 4)
        a, b = random.randint(3, 8), random.randint(3, 8)
        
        return QuestionResult(
            question=f"مثلثان متشابهان، نسبة التشابه 1:{ratio}. إذا كان ضلع {a}، ما المقابل؟",
            expression="",
            answer=str(a * ratio),
            hints=[f"{a} × {ratio} = {a * ratio}"],
            skill_id="similarity",
            difficulty=self.difficulty
        ).to_dict()
