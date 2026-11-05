# DL Project

머신러닝 · 딥러닝 모델을 직접 학습시키고,<br>
Flask 웹 화면에서 바로 써 볼 수 있게 만든 학습 프로젝트 모음입니다.

## 기술 스택

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

---

## 📁 이론 정리

1. [Docker · Flask · HTTP](./theory/docker_flask_http/docker_flask_http.md)

## 📁 기초 연습

- [Flask 기본 예제](./flask/hello.py)

---

<br>

## 🚀 프로젝트

### 🌸 Iris KNN 품종 분류

> 붓꽃 측정값 4개로 품종(Setosa · Versicolor · Virginica)을 맞히는 웹 앱 *(머신러닝 · KNN)*
>
> - 모델: KNN (scikit-learn)
> - 데이터: scikit-learn 내장 Iris 데이터셋
>
> <details>
> <summary>실행 화면</summary>
>
> <img src="./flask/iris_knn_flask/static/images/result_setosa.png" width="400" alt="Iris KNN 실행 화면">
>
> </details>
>
> ![Python](https://img.shields.io/badge/Python-555555?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-555555?style=flat-square&logo=flask&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-555555?style=flat-square&logo=scikitlearn&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-555555?style=flat-square&logo=docker&logoColor=white)
>
> [상세보기 →](./flask/iris_knn_flask/)

<br>

### ✍️ MNIST 손글씨 숫자 인식

> 캔버스에 쓴 숫자를 0부터 9 중에서 맞히는 웹 앱 *(딥러닝 · CNN)*
>
> - 모델: CNN (TensorFlow · Keras)
> - 데이터: MNIST 손글씨 숫자 데이터셋
>
> <details>
> <summary>실행 화면</summary>
>
> <img src="./tensorflow/MNIST/static/image/mnist.png" width="500" alt="MNIST 실행 화면">
>
> </details>
>
> ![Python](https://img.shields.io/badge/Python-555555?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-555555?style=flat-square&logo=flask&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-555555?style=flat-square&logo=tensorflow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-555555?style=flat-square&logo=keras&logoColor=white)
>
> [상세보기 →](./tensorflow/MNIST/)
