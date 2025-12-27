"""
Base generator class and utilities for question generation
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import random
from sympy import symbols, Eq, solve, expand, factor, simplify, sqrt, Rational
from sympy import diff, integrate, limit, sin, cos, tan, log, exp, pi, oo
from sympy import latex

class QuestionGenerator(ABC):
    """Base class for all question generators"""
    
    def __init__(self, difficulty: int = 2):
        """
        Initialize generator with difficulty level
        difficulty: 1 (easy) to 5 (hard)
        """
        self.difficulty = min(max(difficulty, 1), 5)
        self.x = symbols('x')
        self.y = symbols('y')
    
    @abstractmethod
    def generate(self) -> Dict[str, Any]:
        """Generate a question and return dict with question, expression, answer, hints"""
        pass
    
    def to_latex(self, expr) -> str:
        """Convert sympy expression to LaTeX string"""
        return latex(expr)
    
    def get_range(self) -> tuple:
        """Get number range based on difficulty - larger numbers for better challenge"""
        ranges = {
            1: (10, 50),     # Easy: 2-digit numbers
            2: (20, 99),     # Medium: larger 2-digit
            3: (50, 200),    # Medium-hard
            4: (100, 500),   # Hard
            5: (100, 999)    # Very hard: 3-digit
        }
        return ranges.get(self.difficulty, (20, 99))
    
    def random_int(self, exclude_zero: bool = False) -> int:
        """Get random integer based on difficulty"""
        low, high = self.get_range()
        val = random.randint(low, high)
        if exclude_zero and val == 0:
            val = 1
        return val
    
    def random_sign(self) -> int:
        """Random +1 or -1"""
        return random.choice([1, -1])


class QuestionResult:
    """Standard question result format"""
    def __init__(
        self,
        question: str,
        expression: str,
        answer: str,
        hints: List[str],
        skill_id: str,
        difficulty: int,
        question_type: str = "input"
    ):
        self.question = question
        self.expression = expression
        self.answer = answer
        self.hints = hints
        self.skill_id = skill_id
        self.difficulty = difficulty
        self.question_type = question_type
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "question": self.question,
            "expression": self.expression,
            "answer": self.answer,
            "hints": self.hints,
            "skill_id": self.skill_id,
            "difficulty": self.difficulty,
            "type": self.question_type
        }
