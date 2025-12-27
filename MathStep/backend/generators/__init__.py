"""
Question generators module - exports all generators
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.arithmetic import (
    AdditionGenerator,
    SubtractionGenerator,
    MultiplicationGenerator,
    DivisionGenerator,
    IntegerOperationsGenerator
)
from generators.fractions import (
    FractionsGenerator,
    RatiosGenerator,
    PrimeFactorizationGenerator
)
from generators.algebra import (
    LinearEquationsGenerator,
    InequalitiesGenerator,
    DistributivePropertyGenerator,
    ExponentsGenerator,
    SystemsOfEquationsGenerator,
    SlopeLineEquationsGenerator
)
from generators.polynomials import (
    PolynomialsGenerator,
    FactoringGenerator,
    QuadraticEquationsGenerator,
    PythagoreanTheoremGenerator,
    SimilarityGenerator
)
from generators.calculus import (
    LimitsContinuityGenerator,
    DerivativesRulesGenerator,
    ChainRuleGenerator,
    IntegralsGenerator,
    UnitCircleGenerator
)
from generators.functions import (
    FunctionsDomainRangeGenerator,
    InverseCompositeFunctionsGenerator,
    LogarithmsGenerator,
    ComplexNumbersGenerator
)

# Skill ID to Generator mapping
SKILL_GENERATORS = {
    # Level 1 - Arithmetic
    "addition": AdditionGenerator,
    "subtraction": SubtractionGenerator,
    "multiplication": MultiplicationGenerator,
    "division": DivisionGenerator,
    
    # Level 2 - Number Operations
    "integer-operations": IntegerOperationsGenerator,
    "fractions": FractionsGenerator,
    "ratios": RatiosGenerator,
    "prime-factorization": PrimeFactorizationGenerator,
    
    # Level 3 - Pre-Algebra
    "exponents": ExponentsGenerator,
    "distributive-property": DistributivePropertyGenerator,
    "linear-equations": LinearEquationsGenerator,
    "inequalities": InequalitiesGenerator,
    
    # Level 4 - Linear Algebra
    "slope-line-equations": SlopeLineEquationsGenerator,
    "systems-of-equations": SystemsOfEquationsGenerator,
    
    # Level 5 - Polynomials & Geometry
    "polynomials": PolynomialsGenerator,
    "factoring": FactoringGenerator,
    "pythagorean-theorem": PythagoreanTheoremGenerator,
    "similarity": SimilarityGenerator,
    
    # Level 6 - Advanced Algebra
    "complex-numbers": ComplexNumbersGenerator,
    "quadratic-equations": QuadraticEquationsGenerator,
    "functions-domain-range": FunctionsDomainRangeGenerator,
    "inverse-composite-functions": InverseCompositeFunctionsGenerator,
    "logarithms": LogarithmsGenerator,
    
    # Level 7 - Calculus
    "unit-circle": UnitCircleGenerator,
    "limits-continuity": LimitsContinuityGenerator,
    "derivatives-rules": DerivativesRulesGenerator,
    "chain-rule": ChainRuleGenerator,
    "integrals": IntegralsGenerator,
}

# Grade to skills mapping
GRADE_SKILLS = {
    5: ["addition", "subtraction", "multiplication", "division"],
    6: ["addition", "subtraction", "multiplication", "division", "fractions", "ratios"],
    7: ["fractions", "ratios", "integer-operations", "exponents", "prime-factorization"],
    8: ["exponents", "distributive-property", "linear-equations", "inequalities"],
    9: ["linear-equations", "slope-line-equations", "systems-of-equations", "polynomials"],
    10: ["polynomials", "factoring", "quadratic-equations", "functions-domain-range"],
    11: ["quadratic-equations", "complex-numbers", "logarithms", "inverse-composite-functions", "pythagorean-theorem"],
    12: ["logarithms", "unit-circle", "limits-continuity", "derivatives-rules", "chain-rule", "integrals"],
}


def generate_question(skill_id: str, difficulty: int = 2) -> dict:
    """Generate a question for the given skill"""
    generator_class = SKILL_GENERATORS.get(skill_id)
    if not generator_class:
        return {"error": f"Unknown skill: {skill_id}"}
    
    generator = generator_class(difficulty=difficulty)
    return generator.generate()


def get_skills_for_grade(grade: int) -> list:
    """Get list of skills for a given grade"""
    skills = []
    for g in range(5, grade + 1):
        skills.extend(GRADE_SKILLS.get(g, []))
    return list(set(skills))  # Remove duplicates
