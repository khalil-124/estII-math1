"""
MathStep Database Models
User, Progress, and Exam Result models
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class User(Base):
    """User model - stores Google OAuth user info"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    picture = Column(String(500), nullable=True)
    google_id = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    progress = relationship("UserProgress", back_populates="user", cascade="all, delete-orphan")
    exam_results = relationship("ExamResult", back_populates="user", cascade="all, delete-orphan")
    
    # Aggregate stats
    total_questions = Column(Integer, default=0)
    total_correct = Column(Integer, default=0)
    streak = Column(Integer, default=0)
    points = Column(Integer, default=0)
    last_active_date = Column(String(10), nullable=True)  # YYYY-MM-DD


class UserProgress(Base):
    """Progress for each skill per user"""
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    skill_id = Column(String(100), nullable=False, index=True)
    
    total_questions = Column(Integer, default=0)
    correct_answers = Column(Integer, default=0)
    last_answers = Column(JSON, default=list)  # Last 20 answers as boolean array
    mastery_level = Column(String(20), default="locked")  # locked, weak, learning, mastered
    last_practiced = Column(String(10), nullable=True)  # YYYY-MM-DD
    next_review = Column(String(10), nullable=True)  # YYYY-MM-DD for spaced repetition
    
    # Relationship
    user = relationship("User", back_populates="progress")
    
    # Unique constraint: one progress per skill per user
    __table_args__ = (
        {"sqlite_autoincrement": True},
    )


class ExamResult(Base):
    """Diagnostic exam results"""
    __tablename__ = "exam_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    grade = Column(Integer, nullable=False)  # School grade (5-12)
    score = Column(Integer, nullable=False)
    total_questions = Column(Integer, nullable=False)
    percentage = Column(Float, nullable=False)
    
    weak_skills = Column(JSON, default=list)  # List of skill IDs
    strong_skills = Column(JSON, default=list)  # List of skill IDs
    
    taken_at = Column(DateTime, default=datetime.utcnow)
    duration_seconds = Column(Integer, nullable=True)
    
    # Relationship
    user = relationship("User", back_populates="exam_results")
