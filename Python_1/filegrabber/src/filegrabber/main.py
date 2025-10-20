from __future__ import annotations
from pathlib import Path
import requests
from filegrabber.transformer import CsvTransformer


# --- Wyjątki z ćwiczenia II ---
class DownloadError(Exception):
    """Bazowy wyjątek dla błędów pobierania."""


class NotFoundError(DownloadError):
    """Rzucany, gdy serwer zwraca 404."""


class AccessDeniedError(DownloadError):
    """Rzucany, gdy serwer zwraca 403."""


# --- Funkcja pobierająca plik ---
def download_file(url: str, filename: str | None = None) -> Path:
    """
    Pobiera plik spod podanego URL i zapisuje go na dysku.
    Jeśli nie podano nazwy pliku, zapisuje jako 'latest.txt'.
    """
    target = Path(filename or "latest.txt")

    response = requests.get(url, stream=True, timeout=30)

    if response.status_code == 404:
        raise NotFoundError(f"Plik nie został znaleziony: {url}")
    elif response.status_code == 403:
        raise AccessDeniedError(f"Brak dostępu do: {url}")
    elif response.status_code >= 400:
        raise DownloadError(f"Błąd serwera ({response.status_code}) dla: {url}")

    with open(target, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"✅ Zapisano plik: {target.resolve()}")
    return target


# --- Funkcja główna ---
def main() -> None:
    url = "https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv"
    filename = "sample.csv"

    try:
        # pobranie pliku
        download_file(url, filename)

        # transformacja danych CSV
        transformer = CsvTransformer(filename)
        transformer.save_results()

    except NotFoundError as e:
        print(f"❌ Błąd 404: {e}")
    except AccessDeniedError as e:
        print(f"🚫 Błąd 403: {e}")
    except DownloadError as e:
        print(f"⚠️  Inny błąd pobierania: {e}")
    except Exception as e:
        print(f"💥 Nieoczekiwany błąd: {e}")


if __name__ == "__main__":
    main()
