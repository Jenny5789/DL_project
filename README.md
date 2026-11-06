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

<table width="100%">
<tr>
<td width="50%" valign="top">

<a href="./flask/iris_knn_flask/"><img src="./flask/iris_knn_flask/static/images/result_setosa.png" height="240" alt="Iris KNN 실행 화면"></a>

<img src="https://img.shields.io/badge/Machine_Learning-1f3a5f?style=flat" alt="Machine Learning" align="middle"> &nbsp;<sub>2026.10</sub>

### Iris KNN 품종 분류 <a href="./flask/iris_knn_flask/"><img src="images/detail-link.svg" alt="상세보기 →"></a>

`scikit-learn` `Flask` `Docker`

**머신러닝 분류 모델 학습 · 웹 서비스 배포**

- 붓꽃 측정값 4개로 품종 3종 분류 (KNN)
- 입력값 기반 예측 · 품종별 이미지 출력
- Docker 컨테이너 실행 환경 구성

</td>
<td width="50%" valign="top">

<a href="./tensorflow/MNIST/"><img src="./tensorflow/MNIST/static/image/mnist.png" height="240" alt="MNIST 실행 화면"></a>

<img src="https://img.shields.io/badge/Deep_Learning-1f3a5f?style=flat" alt="Deep Learning" align="middle"> &nbsp;<sub>2026.10</sub>

### MNIST 손글씨 숫자 인식 <a href="./tensorflow/MNIST/"><img src="images/detail-link.svg" alt="상세보기 →"></a>

`TensorFlow` `Keras` `Flask` `Docker`

**딥러닝 CNN 모델 구현 · 웹 추론 서비스**

- MNIST 6만 장 학습, Conv 2층 + Dense CNN 설계
- 캔버스 입력 → 28×28 전처리 → 숫자 · 확률 출력
- TensorFlow GPU(CUDA) Docker 학습 환경 구성

</td>
</tr>
</table>
