from pathlib import Path
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from .load_data import load_labels, DATA_ROOT
from .utils import extract_mean_rgb


def build_rgb_dataset(df):
    """
    Tworzy macierz X (średnie RGB) oraz y (hour).
    Radzi sobie z NaN, floatami i złymi wierszami.
    """

    X_list = []
    y_list = []

    for _, row in tqdm(df.iterrows(), total=len(df)):
        rel_path = str(row["filepath"])           # <- Wymuszenie STRING
        if rel_path.lower() == "nan" or rel_path.strip() == "":
            continue

        full_path = DATA_ROOT / rel_path

        feat = extract_mean_rgb(full_path)
        if feat is None:
            continue

        X_list.append(feat)
        y_list.append(int(row["hour"]))

    X = np.vstack(X_list)
    y = np.array(y_list, dtype=np.int64)

    return X, y


if __name__ == "__main__":
    df = load_labels()
    print("Liczba rekordów w labels.csv:", len(df))

    print("Ekstrakcja cech (średnie RGB)...")
    X, y = build_rgb_dataset(df)
    print("Gotowe X shape:", X.shape, "y shape:", y.shape)

    X_tr, X_te, y_tr, y_te = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y if len(np.unique(y)) > 1 else None,
    )

    clf = LogisticRegression(
        max_iter=2000,
        multi_class="multinomial",
        n_jobs=-1,
    )
    clf.fit(X_tr, y_tr)

    y_pred = clf.predict(X_te)
    print("\n=== Wyniki modelu bazowego (średnie RGB) ===")
    print("Accuracy:", accuracy_score(y_te, y_pred))
    print("\nClassification report:")
    print(classification_report(y_te, y_pred))
    print("Macierz pomyłek:")
    print(confusion_matrix(y_te, y_pred))
