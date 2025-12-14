import csv
import time
from pathlib import Path
from typing import Generator, Callable


# --- Dekorator logujący czas działania ---
def log_time(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"⏳ Start funkcji {func.__name__} ...")
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"✅ Zakończono {func.__name__} (czas: {duration:.3f} s)")
        return result
    return wrapper


class CsvTransformer:
    """Prosty proces ETL (Extract–Transform–Load) dla plików CSV."""

    def __init__(self, input_file: str | Path):
        self.input_file = Path(input_file)
        if not self.input_file.exists():
            raise FileNotFoundError(f"Plik {self.input_file} nie istnieje.")

    # --- Generator do czytania pliku linia po linii ---
    def read_rows(self) -> Generator[list[str], None, None]:
        with self.input_file.open(encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                yield row

    # --- Funkcja przetwarzająca (opakowana dekoratorem) ---
    @log_time
    def transform(self):
        values_data = []
        missing_data = []

        for row in self.read_rows():
            try:
                index = int(row[0])
                values = row[1:]
            except (ValueError, IndexError):
                continue

            missing_indices = [i + 1 for i, val in enumerate(values) if val.strip() == "-"]
            filled_values = [float(val) for val in values if val.strip() != "-"]
            total = sum(filled_values)
            avg = total / len(filled_values) if filled_values else 0.0

            values_data.append([index, total, round(avg, 2)])
            missing_data.append([index, ",".join(map(str, missing_indices))])

        return values_data, missing_data

    # --- Zapis danych do plików ---
    def save_results(self, values_file="values.csv", missing_file="missing_values.csv"):
        values_data, missing_data = self.transform()

        with open(values_file, "w", newline="", encoding="utf-8") as vf:
            writer = csv.writer(vf)
            writer.writerow(["numer", "suma", "srednia"])
            writer.writerows(values_data)

        with open(missing_file, "w", newline="", encoding="utf-8") as mf:
            writer = csv.writer(mf)
            writer.writerow(["numer", "brakujace_kolumny"])
            writer.writerows(missing_data)

        print(f"📂 Zapisano {values_file} i {missing_file}")
