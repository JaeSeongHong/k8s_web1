# Nginx 기반 Frontend
FROM nginx:1.25-alpine

# 보안: 불필요한 패키지 제거
RUN apk --no-cache add curl

# Custom Nginx 설정 복사
COPY nginx.conf /etc/nginx/nginx.conf

# HTML 파일 복사
COPY html/ /usr/share/nginx/html/

# 권한 설정
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/health || exit 1

# 포트 노출
EXPOSE 80

# Nginx 실행 (데몬 모드 off)
CMD ["nginx", "-g", "daemon off;"]
