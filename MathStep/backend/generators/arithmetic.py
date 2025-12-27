"""
Arithmetic generators: addition, subtraction, multiplication, division
"""
import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generators.base import QuestionGenerator, QuestionResult

class AdditionGenerator(QuestionGenerator):
    """Generate addition questions"""
    
    def generate(self) -> dict:
        a = self.random_int()
        b = self.random_int()
        
        # Higher difficulty: decimals
        if self.difficulty >= 4:
            a = round(a + random.random(), 1)
            b = round(b + random.random(), 1)
        
        answer = a + b
        
        return QuestionResult(
            question="احسب:",
            expression=f"{a} + {b}",
            answer=str(answer),
            hints=[f"اجمع {a} مع {b}"],
            skill_id="addition",
            difficulty=self.difficulty
        ).to_dict()


class SubtractionGenerator(QuestionGenerator):
    """Generate subtraction questions"""
    
    def generate(self) -> dict:
        a = self.random_int()
        b = self.random_int()
        
        # Ensure positive result for lower difficulties
        if self.difficulty <= 2:
            a, b = max(a, b), min(a, b)
        
        answer = a - b
        
        return QuestionResult(
            question="احسب:",
            expression=f"{a} - {b}",
            answer=str(answer),
            hints=[f"اطرح {b} من {a}"],
            skill_id="subtraction",
            difficulty=self.difficulty
        ).to_dict()


class MultiplicationGenerator(QuestionGenerator):
    """Generate multiplication questions"""
    
    def generate(self) -> dict:
        # Larger ranges for better challenge
        if self.difficulty <= 2:
            a = random.randint(5, 20)
            b = random.randint(5, 15)
        elif self.difficulty == 3:
            a = random.randint(10, 30)
            b = random.randint(5, 20)
        else:
            a = random.randint(15, 50)
            b = random.randint(10, 25)
        
        answer = a * b
        
        return QuestionResult(
            question="احسب:",
            expression=f"{a} \\times {b}",
            answer=str(answer),
            hints=[f"استخدم جدول الضرب أو احسب {a} × {b}"],
            skill_id="multiplication",
            difficulty=self.difficulty
        ).to_dict()


class DivisionGenerator(QuestionGenerator):
    """Generate division questions - ensures clean division"""
    
    def generate(self) -> dict:
        # Generate divisor first, then create dividend that divides evenly
        if self.difficulty <= 2:
            b = random.randint(2, 12)
            quotient = random.randint(2, 12)
        elif self.difficulty == 3:
            b = random.randint(2, 15)
            quotient = random.randint(2, 15)
        else:
            b = random.randint(5, 20)
            quotient = random.randint(5, 20)
        
        a = b * quotient  # Ensures clean division
        
        return QuestionResult(
            question="احسب:",
            expression=f"{a} \\div {b}",
            answer=str(quotient),
            hints=[f"كم مرة يتسع {b} في {a}؟"],
            skill_id="division",
            difficulty=self.difficulty
        ).to_dict()


class IntegerOperationsGenerator(QuestionGenerator):
    """Generate operations with negative numbers"""
    
    def generate(self) -> dict:
        operation = random.choice(['add', 'sub', 'mul', 'div'])
        
        a = self.random_int() * random.choice([1, -1])
        b = self.random_int() * random.choice([1, -1])
        
        if operation == 'add':
            expr = f"({a}) + ({b})"
            answer = a + b
            hint = "تذكر قواعد جمع الأعداد الصحيحة"
        elif operation == 'sub':
            expr = f"({a}) - ({b})"
            answer = a - b
            hint = "طرح سالب = جمع موجب"
        elif operation == 'mul':
            # Keep numbers smaller for multiplication
            a = random.randint(2, 10) * random.choice([1, -1])
            b = random.randint(2, 10) * random.choice([1, -1])
            expr = f"({a}) \\times ({b})"
            answer = a * b
            hint = "سالب × سالب = موجب، سالب × موجب = سالب"
        else:  # div
            b = random.randint(2, 10) * random.choice([1, -1])
            quotient = random.randint(2, 10) * random.choice([1, -1])
            a = b * quotient
            expr = f"({a}) \\div ({b})"
            answer = quotient
            hint = "سالب ÷ سالب = موجب، سالب ÷ موجب = سالب"
        
        return QuestionResult(
            question="احسب:",
            expression=expr,
            answer=str(answer),
            hints=[hint],
            skill_id="integer-operations",
            difficulty=self.difficulty
        ).to_dict()
