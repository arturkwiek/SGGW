# context_experiments.py

# --- 1. Logger ---
class Logger:
    def __enter__(self):
        print("Start sekcji logowania")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Koniec sekcji logowania")
        return False


# --- 2. FileWriter ---
class FileWriter:
    def __init__(self, path, mode="w", encoding="utf-8"):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self._fh = None

    def __enter__(self):
        self._fh = open(self.path, self.mode, encoding=self.encoding)
        return self._fh

    def __exit__(self, exc_type, exc, tb):
        if self._fh and not self._fh.closed:
            self._fh.close()
        if exc_type is not None:
            print(f"Błąd podczas zapisu: {exc}")
            return False
        return False


# --- 3. SafeDivision ---
class SafeDivision:
    def __enter__(self):
        return self

    def divide(self, a, b):
        return a / b

    def __exit__(self, exc_type, exc, tb):
        if exc_type is ZeroDivisionError:
            print("Nie można dzielić przez zero")
            return True
        return False


# --- Testy ---
if __name__ == "__main__":
    print("\n=== Test Logger ===")
    with Logger():
        print("Coś w środku...")

    print("\n=== Test FileWriter ===")
    with FileWriter("test.txt") as f:
        f.write("Linia testowa\n")

    print("\n=== Test SafeDivision ===")
    with SafeDivision() as sd:
        print(sd.divide(10, 2))
        print("Spróbujemy dzielenia przez zero…")
        sd.divide(1, 0)
        print("Program nadal działa.")
