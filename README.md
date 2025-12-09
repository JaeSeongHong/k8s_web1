# DevOps Learning Journey

## 환경 정보
- **Machine**: NUC13ANK (Intel i3-1315U, 16GB RAM)
- **OS**: Ubuntu 24.04.2 LTS
- **Kernel**: 6.11.0-19-generic
- **Docker**: 29.1.2
- **Docker Compose**: v5.0.0
- **Storage Driver**: overlayfs

## 학습 목표
1. 로컬 환경에서 DevOps 전체 사이클 실습
2. Kubernetes 클러스터 구성 및 운영
3. CI/CD 파이프라인 구축
4. IaC 및 GitOps 워크플로우 실습
5. Observability 스택 구축
6. 실무 수준의 인프라 설계 역량 확보

## 프로젝트 구조
```
devops-learning/
├── projects/    # 실습 프로젝트
│   ├── 01-docker-basics/
│   ├── 02-kubernetes/
│   ├── 03-cicd/
│   └── 04-monitoring/
├── scripts/     # 자동화 스크립트
│   ├── setup/
│   ├── backup/
│   └── monitoring/
├── configs/     # 설정 파일
│   ├── docker/
│   ├── k8s/
│   └── terraform/
├── docs/        # 문서 및 노트
│   ├── architecture/
│   ├── runbooks/
│   └── references/
└── tools/       # 유틸리티
    ├── templates/
    └── snippets/
```

## 진행 상황
- [x] 시스템 기본 도구 설치 (git, curl, vim, htop 등)
- [x] Docker 설치 및 설정 (v29.1.2)
- [x] Docker 동작 검증 완료
- [x] 프로젝트 디렉토리 구조 생성
- [ ] Docker 기초 실습
- [ ] Kubernetes 설치
- [ ] CI/CD 파이프라인 구축
- [ ] 모니터링 스택 구축

## Docker 정보
- **컨테이너 런타임**: containerd
- **Storage Driver**: overlayfs
- **첫 컨테이너 실행**: hello-world (성공)

## 참고 자료
- [Docker 공식 문서](https://docs.docker.com/)
- [Kubernetes 공식 문서](https://kubernetes.io/docs/)
- [DevOps Roadmap](https://roadmap.sh/devops)

---
**작성일**: 2025-12-09
