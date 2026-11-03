# DL Project

머신러닝과 딥러닝 학습 프로젝트 모음

## 기술 스택

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)

## 폴더별 프로젝트

### Flask

#### [Iris KNN Flask](./flask/iris_knn_flask/)

붓꽃 측정값을 입력해 KNN 알고리즘으로 품종을 분류하는 Flask 웹 애플리케이션

- 입력값: Sepal Length, Sepal Width, Petal Length, Petal Width
- 출력값: Setosa, Versicolor, Virginica
- 기술: Python, Flask, scikit-learn
- 실행 포트: `5000`

#### [Flask Hello](./flask/hello.py)

Flask 기본 웹 애플리케이션 예제

### TensorFlow

#### [MNIST 숫자 분류](./tensorflow/MNIST/)

손글씨 숫자를 CNN 모델로 학습하고 Flask 웹 화면에서 예측하는 프로젝트

- 데이터셋: MNIST
- 입력값: 캔버스 손글씨 숫자
- 출력값: 숫자 `0`~`9`
- 기술: Python, TensorFlow, Keras, Flask
- 실행 포트: `8888`

### Python

#### [Python 예제](./python/)

Python 기초 및 머신러닝 관련 실습 코드

### Theory

#### [이론 정리](./theory/)

머신러닝과 딥러닝 관련 이론 및 학습 자료

## 프로젝트 실행

각 프로젝트 이름을 클릭하면 해당 폴더로 이동할 수 있습니다. 자세한 실행 방법은 프로젝트별 README를 참고합니다.

### Iris KNN Flask

```bash
cd flask/iris_knn_flask
python app.py
```

접속 주소:

```text
http://127.0.0.1:5000/
```

### MNIST 숫자 분류

```bash
cd tensorflow/MNIST
python app.py
```

접속 주소:

```text
http://127.0.0.1:8888/
```

## 저장소 구조

```text
DL_project/
├─ flask/
│  ├─ hello.py
│  └─ iris_knn_flask/
├─ tensorflow/
│  └─ MNIST/
├─ python/
├─ theory/
└─ README.md
```

## 프로젝트별 README

- [Iris KNN Flask README](./flask/iris_knn_flask/README.md)
- [MNIST README](./tensorflow/MNIST/README.md)

