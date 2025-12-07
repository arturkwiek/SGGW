from pathlib import Path
import cv2
import numpy as np


def extract_mean_rgb(path: Path):
    """
    Wczytuje obraz z podanej ścieżki i zwraca średnie wartości kanałów RGB.
    Zwraca np.ndarray o kształcie (3,) lub None jeśli obrazka nie da się wczytać.
    """
    img = cv2.imread(str(path))
    if img is None:
        return None

    # OpenCV czyta w BGR, konwersja na RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # policz średnie po wszystkich pikselach
    mean_rgb = img.reshape(-1, 3).mean(axis=0)
    return mean_rgb.astype(np.float32)
