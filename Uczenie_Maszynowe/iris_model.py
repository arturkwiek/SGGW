#
# Prosty przykład uczenia maszynowego na zbiorze danych Iris

# Model został przygotowany w oparciu o klasyczny zbiór danych Iris dostępny w UCI Machine Learning Repository,
# Do realizacji zadania wybrano model logistycznej regresji wieloklasowej, ponieważ jest to prosty, dobrze poznany algorytm.
# Dane zostały podzielone na część treningową i testową w proporcji 80/20 z zachowaniem proporcji klas, 
# a następnie poddane standaryzacji, co ułatwia poprawną pracę modelu. 

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import numpy as np
import matplotlib.pyplot as plt

def main():
    # 1. Wczytanie zbioru danych
    iris = load_iris()
    X = iris.data          # cechy (4 kolumny)
    y = iris.target        # etykiety klas (0,1,2)
    class_names = iris.target_names

    print("Kształt X:", X.shape)
    print("Kształt y:", y.shape)
    print("Nazwy klas:", class_names)

    # 2. Podział na zbiór treningowy i testowy
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Standaryzacja cech (średnia 0, odchylenie 1 – pomaga modelowi)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Wybór i trenowanie modelu – logistyczna regresja wieloklasowa
    model = LogisticRegression(
        multi_class="multinomial",
        max_iter=1000,
        random_state=42
    )
    model.fit(X_train_scaled, y_train)

    # 5. Ewaluacja
    y_pred = model.predict(X_test_scaled)

    acc = accuracy_score(y_test, y_pred)
    print(f"\nDokładność (accuracy) na zbiorze testowym: {acc:.3f}")

    print("\nClassification report:")
    print(classification_report(y_test, y_pred, target_names=class_names))

    print("Macierz konfuzji:")
    print(confusion_matrix(y_test, y_pred))

    # (opcjonalnie) prosty wykres 2D – dwie cechy vs gatunek
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=y)  # sepal length vs sepal width
    plt.xlabel("Sepal length [cm]")
    plt.ylabel("Sepal width [cm]")
    plt.title("Iris dataset – wizualizacja 2D")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
