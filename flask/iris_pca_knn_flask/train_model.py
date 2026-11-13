import csv
import json
import pickle
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


RANDOM_STATE = 42
PCA_COMPONENTS = 2
K_CANDIDATES = [1, 3, 5, 7, 9]
PCA_CANDIDATES = [1, 2, 3, 4]

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"
RESULTS_DIR = BASE_DIR / "results"
MODEL_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)


# Iris 데이터 불러오기
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names


# Test 22개 분리
X_temp, X_test, y_temp, y_test = train_test_split(
    X,
    y,
    test_size=22,
    random_state=RANDOM_STATE,
    stratify=y,
)


# Train 105개, Validation 23개 분리
X_train, X_val, y_train, y_val = train_test_split(
    X_temp,
    y_temp,
    test_size=23,
    random_state=RANDOM_STATE,
    stratify=y_temp,
)


print("데이터 개수")
print(f"Train      : {len(X_train)}")
print(f"Validation : {len(X_val)}")
print(f"Test       : {len(X_test)}")
print()


# Validation 데이터로 k 비교
comparison_results = []

for k in K_CANDIDATES:
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("pca", PCA(n_components=PCA_COMPONENTS)),
        ("knn", KNeighborsClassifier(n_neighbors=k)),
    ])

    pipeline.fit(X_train, y_train)
    val_pred = pipeline.predict(X_val)
    val_accuracy = accuracy_score(y_val, val_pred)

    comparison_results.append({
        "k": k,
        "validation_accuracy": float(val_accuracy),
    })

    print(f"k={k} Validation Accuracy: {val_accuracy:.4f}")


# 동률이면 가장 작은 k 선택
best_result = max(
    comparison_results,
    key=lambda result: (result["validation_accuracy"], -result["k"]),
)
best_k = best_result["k"]
best_val_accuracy = best_result["validation_accuracy"]

print()
print(f"선택된 k: {best_k}")
print(f"최고 Validation Accuracy: {best_val_accuracy:.4f}")


# PCA 주성분 수 비교: k=5 고정
pca_comparison_results = []

for components in PCA_CANDIDATES:
    pca_pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("pca", PCA(n_components=components)),
        ("knn", KNeighborsClassifier(n_neighbors=best_k)),
    ])

    pca_pipeline.fit(X_train, y_train)
    pca_val_pred = pca_pipeline.predict(X_val)
    pca_val_accuracy = accuracy_score(y_val, pca_val_pred)

    pca_comparison_results.append({
        "pca_components": components,
        "k": best_k,
        "validation_accuracy": float(pca_val_accuracy),
    })

    print(
        f"PCA components={components}, k={best_k} "
        f"Validation Accuracy: {pca_val_accuracy:.4f}"
    )


# PCA 비교 결과 CSV 저장
pca_comparison_path = RESULTS_DIR / "pca_comparison.csv"
with pca_comparison_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["pca_components", "k", "validation_accuracy"],
    )
    writer.writeheader()
    writer.writerows(pca_comparison_results)


# PCA 비교 그래프 저장
plt.figure(figsize=(7, 4))
plt.plot(
    [item["pca_components"] for item in pca_comparison_results],
    [item["validation_accuracy"] for item in pca_comparison_results],
    marker="o",
)
plt.xticks(PCA_CANDIDATES)
plt.ylim(0, 1.05)
plt.xlabel("Number of PCA Components")
plt.ylabel("Validation Accuracy")
plt.title("PCA Components Comparison")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "pca_comparison.png", dpi=150)
plt.close()


# Train + Validation 데이터로 최종 모델 학습
X_train_final = np.concatenate([X_train, X_val])
y_train_final = np.concatenate([y_train, y_val])

final_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("pca", PCA(n_components=PCA_COMPONENTS)),
    ("knn", KNeighborsClassifier(n_neighbors=best_k)),
])

final_pipeline.fit(X_train_final, y_train_final)


# Test 데이터 최종 평가
test_pred = final_pipeline.predict(X_test)
test_accuracy = accuracy_score(y_test, test_pred)
confusion = confusion_matrix(y_test, test_pred)

print(f"Test Accuracy: {test_accuracy:.4f}")


# 최종 Pipeline 저장
model_path = MODEL_DIR / "iris_pca_knn_pipeline.pkl"
with model_path.open("wb") as file:
    pickle.dump(final_pipeline, file)


# k 비교 결과 CSV 저장
comparison_path = RESULTS_DIR / "k_comparison.csv"
with comparison_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["k", "validation_accuracy"],
    )
    writer.writeheader()
    writer.writerows(comparison_results)


# PCA 설명 분산 계산
scaler = final_pipeline.named_steps["scaler"]
pca = final_pipeline.named_steps["pca"]
scaler.fit(X_train_final)
pca.fit(scaler.transform(X_train_final))

explained_variance = pca.explained_variance_ratio_

# 실험 설정 및 평가 결과 JSON 저장
metrics = {
    "random_state": RANDOM_STATE,
    "train_size": int(len(X_train)),
    "validation_size": int(len(X_val)),
    "test_size": int(len(X_test)),
    "pca_components": PCA_COMPONENTS,
    "pca_candidates": PCA_CANDIDATES,
    "pca_comparison": pca_comparison_results,
    "k_candidates": K_CANDIDATES,
    "best_k": int(best_k),
    "validation_accuracy": float(best_val_accuracy),
    "test_accuracy": float(test_accuracy),
    "pca_explained_variance_ratio": [
        float(value) for value in explained_variance
    ],
    "pca_total_explained_variance": float(explained_variance.sum()),
    "target_names": target_names.tolist(),
}

metrics_path = RESULTS_DIR / "metrics.json"
with metrics_path.open("w", encoding="utf-8") as file:
    json.dump(metrics, file, ensure_ascii=False, indent=2)


# 혼동행렬 이미지 저장
display = ConfusionMatrixDisplay(
    confusion_matrix=confusion,
    display_labels=target_names,
)
display.plot(cmap="Blues")
plt.title("Iris PCA + KNN Confusion Matrix")
plt.tight_layout()
plt.savefig(RESULTS_DIR / "confusion_matrix.png", dpi=150)
plt.close()


# Test 예측 목록 CSV 저장
predictions_path = RESULTS_DIR / "test_predictions.csv"
with predictions_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["sample_index", "actual", "predicted", "correct"],
    )
    writer.writeheader()

    for index, (actual, predicted) in enumerate(zip(y_test, test_pred)):
        writer.writerow({
            "sample_index": index,
            "actual": target_names[actual],
            "predicted": target_names[predicted],
            "correct": bool(actual == predicted),
        })


print()
print("저장 완료")
print(f"- {model_path}")
print(f"- {comparison_path}")
print(f"- {pca_comparison_path}")
print(f"- {RESULTS_DIR / 'pca_comparison.png'}")
print(f"- {metrics_path}")
print(f"- {RESULTS_DIR / 'confusion_matrix.png'}")
print(f"- {predictions_path}")

