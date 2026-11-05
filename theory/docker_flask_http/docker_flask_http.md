# Docker · Flask · HTTP 이론 정리

## 1. Docker 기본 개념

- 애플리케이션과 실행 환경의 컨테이너 단위 패키징
- Windows 환경: WSL(Windows Subsystem for Linux) 연동

### 핵심 구성 요소

- **Docker Engine**: 컨테이너 생성·실행·관리 담당
- **Image**: 컨테이너 실행용 템플릿
- **Container**: 이미지를 실행한 격리 환경
- **Registry**: 이미지 저장·배포 저장소
- 대표 Registry: Docker Hub

### 이미지와 컨테이너 관계

- 이미지: 설계도
- 컨테이너: 이미지 실행 결과
- 컨테이너 특징
  - 호스트 커널 공유
  - 프로세스·파일 시스템 격리
  - 가상 머신 대비 낮은 실행 비용

### Docker 명령어

```bash
docker images
docker ps
docker ps -a
docker pull python:3.12-slim
docker run -d -it -p 8080:8080 --name myweb python:3.12-slim
```

### `docker run` 주요 옵션

| 옵션 | 의미 |
|---|---|
| `-d` | 백그라운드 실행 |
| `-it` | 터미널 상호작용 허용 |
| `-p 호스트포트:컨테이너포트` | 포트 연결 |
| `--name 이름` | 컨테이너 이름 지정 |
| `-v 호스트경로:컨테이너경로` | 볼륨 연결 |
| `--rm` | 종료 시 컨테이너 삭제 |
| `-w 경로` | 작업 디렉터리 지정 |
| `--entrypoint` | 기본 실행 프로그램 변경 |

### 포트와 주소

- `-p 8080:8080`: 호스트 8080 포트와 컨테이너 8080 포트 연결
- `127.0.0.1`: 현재 컴퓨터 지정 loopback 주소
- `0.0.0.0`: 컨테이너의 모든 네트워크 인터페이스 수신 주소

[Docker 스캔 이미지 보기](images/01_docker_basics_and_run_command.jpg)

## 2. Flask 애플리케이션과 컨테이너

- Flask: Python 기반 웹 프레임워크
- 주요 역할
  - HTTP 요청 수신
  - URL과 함수 연결
  - 요청 데이터 처리
  - HTTP 응답 반환

### 컨테이너 실행 예시

```bash
docker run -d -it -p 5000:5000 \
  --name flaskserver \
  -v D:/DL_project/theory:/workspace \
  -w /workspace \
  python:3.12-slim
```

### 컨테이너 내부 명령 실행

```bash
docker exec -it flaskserver /bin/bash
python -m flask --app app run --host=0.0.0.0 --port=5000
```

- `docker exec`: 실행 중인 컨테이너 내부 명령 실행
- 실행 조건: 대상 컨테이너 실행 상태
- 셸 구분
  - Windows: PowerShell 또는 CMD
  - Linux 컨테이너: Bash

### Flask 라우팅

- 라우팅: URL과 실행 함수의 연결

```python
from flask import Flask, request

app = Flask(__name__)

@app.get("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return f"Hello, {name}!"
```

- 요청 주소: `http://127.0.0.1:5000/greet?name=Jenny`
- 실행 함수: `greet()`
- 쿼리 파라미터: `name=Jenny`
- 응답 결과: `Hello, Jenny!`

[Flask 컨테이너·라우팅 스캔 이미지 보기](images/02_flask_container_and_routing.jpg)

## 3. HTTP 요청과 응답

- HTTP: 클라이언트와 서버의 통신 규칙
- 클라이언트 예시: 브라우저, Postman, 다른 프로그램
- 서버 예시: Flask 애플리케이션

### 주요 HTTP 메서드

| 메서드 | 용도 | 예시 |
|---|---|---|
| `GET` | 데이터 조회 | 페이지·목록 조회 |
| `POST` | 데이터 생성·전달 | 로그인·회원가입·폼 제출 |
| `PUT` | 리소스 전체 수정 | 회원 정보 전체 변경 |
| `PATCH` | 리소스 일부 수정 | 회원 이름 변경 |
| `DELETE` | 데이터 삭제 | 게시글 삭제 |

### GET 요청 데이터

- 전달 위치: URL 쿼리 문자열
- Flask 접근 방법: `request.args`

```python
name = request.args.get("name", "Guest")
```

### POST 요청 데이터

- 전달 위치: 요청 본문
- Flask 접근 방법: `request.form`

```python
@app.post("/submit")
def submit():
    user_input = request.form.get("user_input", "")
    return f"받은 값: {user_input}"
```

### HTML 폼 전송

```html
<form method="post" action="/submit">
  <input name="user_input" />
  <button type="submit">전송</button>
</form>
```

### HTTP 상태 코드

- **2xx 성공**: `200 OK`, `201 Created`
- **3xx 리다이렉션**: 주소 이동·캐시 안내
- **4xx 클라이언트 오류**
  - `400 Bad Request`: 잘못된 요청
  - `401 Unauthorized`: 인증 필요
  - `403 Forbidden`: 접근 거부
  - `404 Not Found`: 리소스 없음
  - `405 Method Not Allowed`: 허용되지 않은 메서드
- **5xx 서버 오류**
  - `500 Internal Server Error`: 서버 내부 오류
  - `502 Bad Gateway`: 게이트웨이 오류

### Postman

- GET·POST 요청 전송 도구
- 응답 상태 코드 확인
- 응답 본문 확인
- Flask 서버 동작 검증

[HTTP 메서드·POST·상태 코드 스캔 이미지 보기](images/03_http_methods_post_request_and_status_codes.jpg)

## 4. 전체 요청 흐름

1. 클라이언트의 URL·HTTP 메서드 요청
2. 호스트 포트에서 컨테이너 포트로 전달
3. Flask 라우터의 URL·메서드 매칭
4. 함수의 요청 데이터 처리
   - GET: `request.args`
   - POST: `request.form`
5. Flask의 응답 본문·상태 코드 반환

## 5. 구성 요소별 역할

| 구성 요소 | 역할 |
|---|---|
| Docker | 실행 환경 구성·격리 |
| Image | 실행 환경 템플릿 |
| Container | 애플리케이션 실행 단위 |
| Flask | 요청 처리·응답 생성 |
| HTTP | 클라이언트·서버 통신 규칙 |
| Postman | API 요청·응답 검증 |

## 6. 확인 항목

- Flask 서버의 `0.0.0.0` 바인딩
- Docker 포트 매핑과 Flask 포트의 일치
- 소스 코드 공유용 볼륨 마운트
- 개발 환경의 Flask 개발 서버 사용
- 운영 환경의 Gunicorn 등 WSGI 서버 검토
