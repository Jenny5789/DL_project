# Iris KNN Flask

## 프로젝트 소개

- 붓꽃(Iris)의 측정값을 입력받아 품종을 예측하는 Flask 웹 애플리케이션
- KNN(K-Nearest Neighbors) 알고리즘 사용
- 예측 대상 품종
  - `setosa`
  - `versicolor`
  - `virginica`
- 입력값
  - 꽃받침 길이
  - 꽃받침 너비
  - 꽃잎 길이
  - 꽃잎 너비
  - 단위: cm
- 예측 결과
  - 품종 이름
  - 품종별 꽃 이미지

## 기본 기능: 이미지 추가 전

- Iris 측정값만 이용해 품종을 예측하는 기본 기능
- KNN 모델 학습과 Flask 예측 화면을 먼저 구현
- 예측 결과는 품종 이름 텍스트로 출력

### 1. Iris 데이터셋 준비

- `scikit-learn`에서 제공하는 Iris 데이터셋 사용
- 각 데이터에는 다음 4개의 측정값이 포함됨
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- 각 데이터에는 정답 품종도 포함됨
  - `setosa`
  - `versicolor`
  - `virginica`

### 2. KNN 모델 학습

- `train_model.py` 실행
- Iris 데이터셋 불러오기
- 전체 데이터를 학습 데이터와 테스트 데이터로 분리
- KNN 분류기 생성
  - 이웃 수: 3
- 4개의 측정값과 품종 정답을 이용해 모델 학습
- 학습된 모델을 피클 파일로 저장
  - 저장 위치: `model/iris_model.pkl`

### 3. Flask 앱 실행

- `app.py` 실행
- Flask 앱이 `model/iris_model.pkl`을 불러옴
- 사용자가 웹 화면에서 4개의 측정값을 입력
- 입력값을 숫자로 변환
- 입력값을 2차원 배열로 구성
- KNN 모델에 입력값 전달
- 모델이 품종 번호를 반환
- 품종 번호를 품종 이름으로 변환

### 4. 이미지 추가 전 결과

- 예측 결과를 텍스트로만 표시
- 처리 흐름

```text
측정값 입력
  -> 입력값 숫자 변환
  -> KNN 모델에 전달
  -> 품종 예측
  -> 품종 이름 텍스트 출력
```

## 응용 기능: 이미지 추가 과정

- 기본 KNN 분류 기능이 동작한 후 추가한 응용 기능
- 기존 모델의 학습 방식과 예측 방식은 유지
- 예측 결과를 더 쉽게 이해할 수 있도록 품종별 이미지 출력 기능 추가

### 1. 품종별 이미지 준비

- 공개 이미지 출처에서 품종별 이미지 다운로드
- 준비한 이미지
  - `setosa.jpg`
  - `versicolor.jpg`
  - `virginica.jpg`
- 꽃이 크게 보이는 접사 이미지 사용

### 2. 이미지 파일 저장

- Flask의 정적 파일 폴더에 이미지 저장
- 저장 위치

```text
static/images/setosa.jpg
static/images/versicolor.jpg
static/images/virginica.jpg
```

### 3. 품종과 이미지 경로 연결

- `app.py`에 품종별 이미지 경로를 등록
- 예시

```python
iris_images = {
    'setosa': 'images/setosa.jpg',
    'versicolor': 'images/versicolor.jpg',
    'virginica': 'images/virginica.jpg',
}
```

### 4. 예측 결과에 맞는 이미지 선택

- 모델이 품종 이름 반환
- 반환된 품종 이름을 이미지 경로와 연결
- 예시
  - `setosa` -> `images/setosa.jpg`
  - `versicolor` -> `images/versicolor.jpg`
  - `virginica` -> `images/virginica.jpg`

## 응용 기능 적용 후

### 1. 변경된 예측 처리

- KNN 모델의 학습 방법은 변경하지 않음
- KNN 모델의 입력값도 변경하지 않음
- 기존처럼 측정값 4개만 사용해 품종 예측
- 예측된 품종 이름을 이용해 이미지 경로 추가 선택

### 2. 변경된 화면 처리

- `templates/index.html`에 결과 이미지 영역 추가
- Flask의 `url_for()`로 `static/images/` 안의 이미지 주소 생성
- 예측 품종 이름 출력
- 예측 품종에 해당하는 이미지 출력
- 입력값 단위인 `cm` 표시

### 3. 이미지 추가 후 처리 흐름

```text
측정값 입력
  -> 입력값 숫자 변환
  -> KNN 모델에 전달
  -> 품종 예측
  -> 품종 이름 결정
  -> 품종별 이미지 경로 선택
  -> 품종 이름과 이미지 함께 출력
```

## 이미지와 모델의 관계

- 이미지
  - KNN 모델 학습에 사용하지 않음
  - 예측 결과를 보여주는 화면 요소
  - 품종을 시각적으로 설명하는 용도
- KNN 모델
  - Iris 측정 데이터로만 학습
  - 꽃받침·꽃잎 측정값 4개로 품종 예측
- 결론
  - 이미지 추가는 모델 학습 방식의 변경이 아님
  - 예측 결과 표시 방식의 확장임

## 변경된 파일

- `app.py`
  - 품종별 이미지 경로 등록
  - 예측 결과에 맞는 이미지 경로 선택
- `templates/index.html`
  - 예측 결과 이미지 표시
  - 입력 단위 `cm` 표시
- `static/images/`
  - 품종별 이미지 저장
- `model/iris_model.pkl`
  - KNN 학습 결과를 저장한 피클 파일
- `README.md`
  - 프로젝트 과정과 이미지 추가 전후 차이 정리

## 실행 방법

```powershell
cd D:\dlproject\flask\iris_knn_flask
python train_model.py
python app.py
```

- 브라우저 접속: `http://127.0.0.1:5000/`
- 모델을 다시 학습하지 않는 경우에는 `python app.py`만 실행 가능
