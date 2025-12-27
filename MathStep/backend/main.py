import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sympy import sympify, simplify
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
import traceback

from generators import generate_question, get_skills_for_grade, SKILL_GENERATORS, GRADE_SKILLS

app = FastAPI(title="MathStep API", version="2.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
class GradeRequest(BaseModel):
    student_answer: str
    correct_answer: str

class GradeResponse(BaseModel):
    is_correct: bool
    message: str

class QuestionRequest(BaseModel):
    skill_id: str
    difficulty: int = 2

class QuestionResponse(BaseModel):
    question: str
    expression: str
    answer: str
    hints: List[str]
    skill_id: str
    difficulty: int
    type: str


# Existing grading endpoint
@app.post("/grade", response_model=GradeResponse)
async def grade_answer(request: GradeRequest):
    try:
        student_expr = sympify(request.student_answer, evaluate=False)
        correct_expr = sympify(request.correct_answer, evaluate=False)
        
        diff = simplify(student_expr - correct_expr)
        is_correct = diff == 0
        
        if is_correct:
            return GradeResponse(is_correct=True, message="أحسنت! إجابة صحيحة 🎉")
        else:
            return GradeResponse(is_correct=False, message="حاول مرة أخرى")
    except Exception as e:
        print(f"Error: {e}")
        return GradeResponse(is_correct=False, message="تعذر فهم الإجابة")


# NEW: Generate question endpoint
@app.post("/generate-question", response_model=QuestionResponse)
async def generate_question_endpoint(request: QuestionRequest):
    """Generate a unique question for a skill"""
    try:
        result = generate_question(request.skill_id, request.difficulty)
        
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        
        return QuestionResponse(**result)
    except Exception as e:
        print(f"Error generating question: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


# NEW: Get skills for grade
@app.get("/skills-for-grade/{grade}")
async def skills_for_grade(grade: int):
    """Get list of skills appropriate for a school grade"""
    if grade < 5 or grade > 12:
        raise HTTPException(status_code=400, detail="Grade must be between 5 and 12")
    
    skills = get_skills_for_grade(grade)
    return {"grade": grade, "skills": skills}


# NEW: Get all available skills
@app.get("/skills")
async def get_all_skills():
    """Get list of all available skills"""
    return {"skills": list(SKILL_GENERATORS.keys())}


# NEW: Generate exam questions
@app.post("/generate-exam")
async def generate_exam(grade: int, num_questions: int = 15):
    """Generate a set of exam questions for a grade"""
    skills = get_skills_for_grade(grade)
    questions = []
    
    import random
    selected_skills = random.choices(skills, k=num_questions)
    
    for skill_id in selected_skills:
        difficulty = random.randint(2, 3)
        q = generate_question(skill_id, difficulty)
        questions.append(q)
    
    return {"grade": grade, "questions": questions}


@app.get("/")
async def root():
    return {"message": "MathStep API v2.0 - Question Generation Ready"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
