import base64
import io
import pickle

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, request
from sklearn.datasets import load_iris


app = Flask(__name__)

with open("model/iris_pca_knn_pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)

iris = load_iris()
target_names = iris.target_names


def create_pca_plot(input_pca=None):
    scaler = pipeline.named_steps["scaler"]
    pca = pipeline.named_steps["pca"]
    iris_pca = pca.transform(scaler.transform(iris.data))

    colors = ["#e76f51", "#2a9d8f", "#457b9d"]
    fig, ax = plt.subplots(figsize=(7, 5))

    for class_id, name in enumerate(target_names):
        points = iris_pca[iris.target == class_id]
        ax.scatter(
            points[:, 0],
            points[:, 1],
            label=name,
            color=colors[class_id],
            alpha=0.75,
            edgecolors="white",
            linewidths=0.5,
        )

    if input_pca is not None:
        ax.scatter(
            input_pca[0, 0],
            input_pca[0, 1],
            marker="*",
            s=260,
            color="#111827",
            edgecolors="white",
            linewidths=1.2,
            label="Input data",
            zorder=5,
        )

    ax.set_title("Iris PCA 2D Scatter Plot")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()

    image = io.BytesIO()
    fig.savefig(image, format="png", dpi=140)
    plt.close(fig)
    return base64.b64encode(image.getvalue()).decode("utf-8")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    plot_image = create_pca_plot()

    if request.method == "POST":
        try:
            values = [
                float(request.form["sepal_length"]),
                float(request.form["sepal_width"]),
                float(request.form["petal_length"]),
                float(request.form["petal_width"]),
            ]
            input_data = np.array([values], dtype=float)
            prediction_id = int(pipeline.predict(input_data)[0])
            probabilities = pipeline.predict_proba(input_data)[0]
            input_pca = pipeline[:-1].transform(input_data)

            result = {
                "name": target_names[prediction_id],
                "image": f"images/{target_names[prediction_id]}.jpg",
                "probability": float(probabilities[prediction_id]),
                "pc1": float(input_pca[0, 0]),
                "pc2": float(input_pca[0, 1]),
            }
            plot_image = create_pca_plot(input_pca)
        except (KeyError, ValueError) as exc:
            error = f"입력값을 확인하세요: {exc}"

    return render_template(
        "index.html",
        result=result,
        error=error,
        plot_image=plot_image,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
