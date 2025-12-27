"""
MathStep User Routes
API endpoints for user management and progress sync
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from database import get_db
from models import User, UserProgress, ExamResult

router = APIRouter(prefix="/users", tags=["users"])


# ==========================================
# Pydantic Schemas
# ==========================================

class GoogleUserData(BaseModel):
    """Data from Google OAuth"""
    email: str
    name: str
    picture: Optional[str] = None
    google_id: str


class SkillProgressData(BaseModel):
    """Progress data for a single skill"""
    skill_id: str
    total_questions: int
    correct_answers: int
    last_answers: List[bool]
    mastery_level: str
    last_practiced: Optional[str] = None
    next_review: Optional[str] = None


class UserProgressSync(BaseModel):
    """Full progress sync from frontend"""
    total_questions: int
    total_correct: int
    streak: int
    points: int
    last_active_date: Optional[str] = None
    skills: List[SkillProgressData]


class ExamResultData(BaseModel):
    """Exam result data"""
    grade: int
    score: int
    total_questions: int
    weak_skills: List[str]
    strong_skills: List[str]
    duration_seconds: Optional[int] = None


# ==========================================
# Routes
# ==========================================

@router.post("/sync")
async def sync_user(user_data: GoogleUserData, db: Session = Depends(get_db)):
    """
    Sync user from Google OAuth.
    Creates new user or returns existing one.
    """
    # Check if user exists
    user = db.query(User).filter(User.google_id == user_data.google_id).first()
    
    if user:
        # Update last login
        user.last_login = datetime.utcnow()
        user.name = user_data.name
        user.picture = user_data.picture
        db.commit()
    else:
        # Create new user
        user = User(
            email=user_data.email,
            name=user_data.name,
            picture=user_data.picture,
            google_id=user_data.google_id,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "picture": user.picture,
        "created_at": user.created_at.isoformat(),
    }


@router.get("/{user_id}/progress")
async def get_user_progress(user_id: int, db: Session = Depends(get_db)):
    """Get all progress data for a user"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get skill progress
    progress_records = db.query(UserProgress).filter(UserProgress.user_id == user_id).all()
    
    skills = {}
    for p in progress_records:
        skills[p.skill_id] = {
            "skillId": p.skill_id,
            "totalQuestions": p.total_questions,
            "correctAnswers": p.correct_answers,
            "lastAnswers": p.last_answers or [],
            "masteryLevel": p.mastery_level,
            "lastPracticed": p.last_practiced,
            "nextReview": p.next_review,
        }
    
    # Get exam history
    exams = db.query(ExamResult).filter(ExamResult.user_id == user_id).order_by(ExamResult.taken_at.desc()).limit(10).all()
    
    exam_history = [
        {
            "date": e.taken_at.isoformat(),
            "grade": e.grade,
            "score": e.score,
            "totalQuestions": e.total_questions,
            "weakSkills": e.weak_skills or [],
            "strongSkills": e.strong_skills or [],
        }
        for e in exams
    ]
    
    return {
        "totalQuestionsAnswered": user.total_questions,
        "totalCorrectAnswers": user.total_correct,
        "streak": user.streak,
        "points": user.points,
        "lastActiveDate": user.last_active_date,
        "skills": skills,
        "badges": [],  # TODO: implement badges
        "examHistory": exam_history,
    }


@router.post("/{user_id}/progress")
async def save_user_progress(user_id: int, progress: UserProgressSync, db: Session = Depends(get_db)):
    """Save/update user progress"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update user stats
    user.total_questions = progress.total_questions
    user.total_correct = progress.total_correct
    user.streak = progress.streak
    user.points = progress.points
    user.last_active_date = progress.last_active_date
    
    # Update skill progress
    for skill_data in progress.skills:
        # Find existing or create new
        skill_progress = db.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.skill_id == skill_data.skill_id
        ).first()
        
        if skill_progress:
            skill_progress.total_questions = skill_data.total_questions
            skill_progress.correct_answers = skill_data.correct_answers
            skill_progress.last_answers = skill_data.last_answers
            skill_progress.mastery_level = skill_data.mastery_level
            skill_progress.last_practiced = skill_data.last_practiced
            skill_progress.next_review = skill_data.next_review
        else:
            skill_progress = UserProgress(
                user_id=user_id,
                skill_id=skill_data.skill_id,
                total_questions=skill_data.total_questions,
                correct_answers=skill_data.correct_answers,
                last_answers=skill_data.last_answers,
                mastery_level=skill_data.mastery_level,
                last_practiced=skill_data.last_practiced,
                next_review=skill_data.next_review,
            )
            db.add(skill_progress)
    
    db.commit()
    return {"success": True}


@router.post("/{user_id}/exam")
async def save_exam_result(user_id: int, result: ExamResultData, db: Session = Depends(get_db)):
    """Save exam result"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    exam = ExamResult(
        user_id=user_id,
        grade=result.grade,
        score=result.score,
        total_questions=result.total_questions,
        percentage=round(result.score / result.total_questions * 100, 1) if result.total_questions > 0 else 0,
        weak_skills=result.weak_skills,
        strong_skills=result.strong_skills,
        duration_seconds=result.duration_seconds,
    )
    db.add(exam)
    db.commit()
    
    return {"success": True, "exam_id": exam.id}
