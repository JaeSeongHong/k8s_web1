-- DevOps Learning Database 초기화 스크립트

-- 방문자 카운트 테이블 생성
CREATE TABLE IF NOT EXISTS visitors (
    id INTEGER PRIMARY KEY,
    count INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 초기 데이터 삽입
INSERT INTO visitors (id, count) VALUES (1, 0)
ON CONFLICT (id) DO NOTHING;

-- 인덱스 생성 (성능 최적화)
CREATE INDEX IF NOT EXISTS idx_visitors_id ON visitors(id);

-- 권한 설정
GRANT ALL PRIVILEGES ON TABLE visitors TO devops_user;
