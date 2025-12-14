# models.py
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

# Tworzymy "bazową" klasę dla modeli
Base = declarative_base()

# --- 1. Tabela Experiment ---
class Experiment(Base):
    __tablename__ = "experiment"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    type = Column(Integer)
    finished = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Experiment(id={self.id}, title={self.title}, finished={self.finished})>"


# --- 2. Tabela DataPoint ---
class DataPoint(Base):
    __tablename__ = "data_point"

    id = Column(Integer, primary_key=True)
    real_value = Column(Float)
    target_value = Column(Float)

    def __repr__(self):
        return f"<DataPoint(id={self.id}, real={self.real_value}, target={self.target_value})>"


# --- Konfiguracja bazy SQLite ---
engine = create_engine("sqlite:///experiments.db", echo=True)

# Tworzymy tabele w bazie
Base.metadata.create_all(engine)
