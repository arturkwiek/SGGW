# exercise3.py
import random
from sqlalchemy import create_engine, update, delete
from sqlalchemy.orm import Session
from models import Experiment, DataPoint, Base

# Połączenie z istniejącą bazą
engine = create_engine("sqlite:///experiments.db", echo=True)

# 1. Dodaj 2 wiersze do tabeli Experiment
with Session(engine) as session:
    exp1 = Experiment(title="Eksperyment 1", type=1)
    exp2 = Experiment(title="Eksperyment 2", type=2)
    session.add_all([exp1, exp2])
    session.commit()
    print("\nDodano eksperymenty:", exp1, exp2)

# 2. Dodaj 10 wierszy do tabeli DataPoint
with Session(engine) as session:
    datapoints = [
        DataPoint(real_value=random.random(), target_value=random.random())
        for _ in range(10)
    ]
    session.add_all(datapoints)
    session.commit()
    print("\nDodano 10 punktów danych.")

# 3. Pobierz dodane dane i wyświetl informacje
with Session(engine) as session:
    experiments = session.query(Experiment).all()
    datapoints = session.query(DataPoint).all()

    print("\nEksperymenty w bazie:")
    for e in experiments:
        print(f" - {e.id}: {e.title}, finished={e.finished}")

    print("\nDataPoints w bazie:")
    for d in datapoints:
        print(f" - id={d.id}, real={d.real_value:.3f}, target={d.target_value:.3f}")

# 4. Zaktualizuj wszystkie wiersze Experiment (finished=True)
with Session(engine) as session:
    session.query(Experiment).update({Experiment.finished: True})
    session.commit()
    print("\nZaktualizowano wszystkie eksperymenty → finished=True")

# 5. Usuń wszystkie dane z obu tabel
with Session(engine) as session:
    session.query(DataPoint).delete()
    session.query(Experiment).delete()
    session.commit()
    print("\nUsunięto wszystkie dane z obu tabel.")
