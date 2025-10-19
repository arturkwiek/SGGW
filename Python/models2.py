# models.py
from datetime import datetime
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Experiment(Base):
    __tablename__ = "experiment"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    type = Column(Integer)
    finished = Column(Boolean, default=False)

    # relacja 1->N (ORM-owa kaskada kasowania w Pythonie)
    data_points = relationship(
        "DataPoint",
        back_populates="experiment",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Experiment(id={self.id}, title={self.title}, finished={self.finished})>"


class DataPoint(Base):
    __tablename__ = "data_point"

    id = Column(Integer, primary_key=True)
    real_value = Column(Float)
    target_value = Column(Float)

    # klucz obcy do Experiment.id
    experiment_id = Column(Integer, ForeignKey("experiment.id"), nullable=False)
    experiment = relationship("Experiment", back_populates="data_points")

    def __repr__(self):
        return f"<DataPoint(id={self.id}, exp={self.experiment_id}, real={self.real_value}, target={self.target_value})>"


# --- silnik + tworzenie bazy ---
engine = create_engine("sqlite:///experiments.db", echo=True)
Base.metadata.create_all(engine)
