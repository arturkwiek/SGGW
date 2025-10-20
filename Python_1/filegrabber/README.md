# README

````markdown
# 🧩 Filegrabber – projekt Python (SGGW)

Prosty projekt typu **ETL (Extract–Transform–Load)** stworzony w ramach zajęć z języka Python.  
Aplikacja pobiera plik CSV z internetu, przetwarza dane i zapisuje wyniki do nowych plików.

---

## ⚙️ Uruchomienie

W katalogu projektu:
```bash
poetry install
poetry run grab
````

Program:

1. Pobiera plik `sample.csv` z sieci,
2. Obsługuje błędy (403, 404, 5xx),
3. Oblicza sumę i średnią wartości w każdym wierszu,
4. Tworzy dwa pliki wynikowe:

   * `values.csv` – numer, suma, średnia
   * `missing_values.csv` – brakujące kolumny

---

## 🧠 Technologie

* Python 3.12
* Poetry
* Requests
* Dekoratory i klasy wyjątków

---