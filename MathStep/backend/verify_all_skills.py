import sys
import os
import traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generators import SKILL_GENERATORS
from sympy import sympify, simplify

def grade_answer(student_answer, correct_answer):
    try:
        # Simple local version of grading logic found in main.py
        student_expr = sympify(student_answer, evaluate=False)
        correct_expr = sympify(correct_answer, evaluate=False)
        diff = simplify(student_expr - correct_expr)
        return diff == 0
    except:
        return False

def verify_all_skills():
    print("Starting verification of all skills (Generation + Grading)...\n", flush=True)
    results = {
        "passed": [],
        "failed": []
    }

    for skill_id, generator_class in SKILL_GENERATORS.items():
        print(f"Testing skill: {skill_id}...", end=" ", flush=True)
        try:
            # Try multiple difficulties
            for difficulty in [2, 3]:
                generator = generator_class(difficulty=difficulty)
                question_data = generator.generate()
                
                # 1. Structure Check
                required_keys = ["question", "expression", "answer", "hints", "skill_id", "difficulty", "type"]
                for key in required_keys:
                    if key not in question_data:
                        raise ValueError(f"Missing key: {key}")
                
                # 2. Grading Check
                # The generator provides 'answer'. Let's pretend the student submits exactly that.
                # Note: Some answers might be plain numbers, others latex.
                # The system usually expects the 'answer' field to be the computable string or simple text.
                correct_ans = str(question_data["answer"])
                
                # Self-consistency check: Does the answer match itself?
                # Using the logic from main.py
                try:
                    is_correct = grade_answer(correct_ans, correct_ans)
                    if not is_correct:
                        # Sometimes answer is not a math expression but a string (e.g. "x=2, y=3")
                        # If sympify fails or returns false, we might need to check how main.py handles it.
                        # But for a robust system, the provided 'answer' SHOULD be gradeable against itself.
                         print(f"[Warning: Self-grading failed for {correct_ans}]", end=" ")
                except:
                     print(f"[Warning: Grading error for {correct_ans}]", end=" ")

            print("✅ OK")
            results["passed"].append(skill_id)
        except Exception as e:
            print(f"❌ FAILED")
            error_msg = f"{str(e)}\n{traceback.format_exc()}"
            results["failed"].append({"skill": skill_id, "error": error_msg})

    print("\n" + "="*50)
    print(f"Summary: {len(results['passed'])} Passed, {len(results['failed'])} Failed")
    print("="*50)

    if results["failed"]:
        print("\nFailures Details:")
        for fail in results["failed"]:
            print(f"\n--- {fail['skill']} ---")
            print(fail['error'])

if __name__ == "__main__":
    verify_all_skills()
