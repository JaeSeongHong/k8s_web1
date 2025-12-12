# Nginx 기반 Frontend - 최적화 버전
FROM nginx:1.25-alpine

# 필수 도구만 설치
RUN apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

# Nginx 설정 복사
COPY nginx.conf /etc/nginx/nginx.conf

# HTML 파일 복사
COPY html/ /usr/share/nginx/html/

# 권한 설정
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/health || exit 1

EXPOSE 80

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]
