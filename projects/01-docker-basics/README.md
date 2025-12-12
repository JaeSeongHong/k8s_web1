# Docker 기초 실습: 3-Tier 웹 애플리케이션

## 🎯 학습 목표
- Docker 이미지 빌드 및 관리
- Docker Compose로 멀티 컨테이너 구성
- 컨테이너 간 네트워크 통신
- 데이터 볼륨 관리
- Health Check 및 로깅

## 🏗️ 아키텍처
```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ :8080
┌──────▼──────────┐
│    Frontend     │
│  (Nginx:80)     │
└──────┬──────────┘
       │ /api/*
┌──────▼──────────┐
│    Backend      │
│  (Flask:5000)   │
└──────┬──────────┘
       │
┌──────▼──────────┐
│    Database     │
│ (PostgreSQL)    │
└─────────────────┘
```

## 📦 기술 스택
- **Frontend**: Nginx 1.25 + HTML/CSS/JavaScript
- **Backend**: Python 3.12 + Flask + Gunicorn
- **Database**: PostgreSQL 16
- **Orchestration**: Docker Compose 5.0

## 🚀 실행 방법

### 1. 빌드 및 실행
```bash
# 모든 서비스 빌드 및 시작
docker compose up -d --build

# 로그 확인
docker compose logs -f

# 특정 서비스 로그
docker compose logs -f backend
```

### 2. 접속
- **웹 애플리케이션**: http://localhost:8080
- **Backend API**: http://localhost:5000/health
- **API 테스트**: http://localhost:5000/api/visitors

### 3. 상태 확인
```bash
# 컨테이너 상태
docker compose ps

# 헬스체크 확인
docker inspect devops-backend | grep -A 5 Health

# 네트워크 확인
docker network ls
docker network inspect 01-docker-basics_app-network
```

### 4. 종료
```bash
# 서비스 중지
docker compose stop

# 서비스 중지 및 컨테이너 제거
docker compose down

# 볼륨까지 삭제 (데이터 초기화)
docker compose down -v
```

## 🔍 학습 포인트

### 1. Dockerfile 베스트 프랙티스
- Multi-stage build (필요시)
- 최소 베이스 이미지 사용 (alpine, slim)
- 레이어 캐싱 최적화
- 비root 사용자 실행 (보안)
- Health check 구현

### 2. Docker Compose
- 서비스 의존성 관리 (`depends_on`)
- Health check 기반 시작 순서 제어
- 환경 변수 관리
- 볼륨 마운트
- 네트워크 격리

### 3. 보안
- 비root 사용자 실행
- 환경 변수로 비밀 정보 관리
- 네트워크 격리
- 읽기 전용 볼륨 마운트

### 4. 운영
- Health check 설정
- 재시작 정책 (`restart`)
- 로그 관리
- 리소스 제한 (추후 추가)

## 📊 테스트 시나리오

### API 테스트
```bash
# 방문자 수 조회
curl http://localhost:5000/api/visitors

# 방문자 수 증가
curl -X POST http://localhost:5000/api/visitors

# Health check
curl http://localhost:5000/health
```

### 데이터베이스 직접 접속
```bash
docker exec -it devops-database psql -U devops_user -d devops_db
```

SQL 쿼리:
```sql
SELECT * FROM visitors;
UPDATE visitors SET count = 100 WHERE id = 1;
```

## 🐛 트러블슈팅

### 컨테이너가 시작되지 않을 때
```bash
# 로그 확인
docker compose logs backend

# 특정 컨테이너 디버그
docker exec -it devops-backend /bin/sh
```

### 네트워크 문제
```bash
# 네트워크 재생성
docker compose down
docker network prune
docker compose up -d
```

### 데이터베이스 연결 실패
```bash
# DB 헬스체크 확인
docker inspect devops-database | grep -A 10 Health

# DB 로그 확인
docker compose logs database
```

## 📚 다음 단계
- [ ] 환경별 설정 분리 (.env 파일)
- [ ] 리소스 제한 추가
- [ ] 로그 수집 (Loki/Fluentd)
- [ ] Prometheus 메트릭 추가
- [ ] Kubernetes로 마이그레이션

---
**작성일**: 2025-12-09
**학습자**: JaeSeongHong
