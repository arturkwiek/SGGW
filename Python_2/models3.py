# models.py
from datetime import datetime
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import event
from sqlalchemy.engine import Engine

Base = declarative_base()
engine = create_engine("sqlite:///experiments.db", echo=True)

@event.listens_for(Engine, "connect")
def set_sqlite_fk(dbapi_conn, _):
    cur = dbapi_conn.cursor()
    cur.execute("PRAGMA foreign_keys=ON")
    cur.close()

class Experiment(Base):
    __tablename__ = "experiment"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    type = Column(Integer)
    finished = Column(Boolean, default=False)
    data_points = relationship("DataPoint", back_populates="experiment",
                               cascade="all, delete-orphan")

class DataPoint(Base):
    __tablename__ = "data_point"
    id = Column(Integer, primary_key=True)
    real_value = Column(Float)
    target_value = Column(Float)
    experiment_id = Column(Integer, ForeignKey("experiment.id", ondelete="CASCADE"), nullable=False)
    experiment = relationship("Experiment", back_populates="data_points")
