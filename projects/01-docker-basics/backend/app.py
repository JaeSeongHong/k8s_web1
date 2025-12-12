from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'database'),
    'database': os.getenv('DB_NAME', 'devops_db'),
    'user': os.getenv('DB_USER', 'devops_user'),
    'password': os.getenv('DB_PASSWORD', 'devops_pass')
}

def get_db_connection():
    """데이터베이스 연결"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"DB Connection Error: {e}")
        return None

@app.route('/health', methods=['GET'])
def health_check():
    """헬스체크 엔드포인트"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'backend-api'
    }), 200

@app.route('/api/visitors', methods=['GET'])
def get_visitors():
    """방문자 수 조회"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT count FROM visitors WHERE id = 1')
        result = cursor.fetchone()
        count = result[0] if result else 0
        cursor.close()
        conn.close()
        
        return jsonify({
            'visitors': count,
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/visitors', methods=['POST'])
def increment_visitors():
    """방문자 수 증가"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO visitors (id, count) VALUES (1, 1)
            ON CONFLICT (id) DO UPDATE SET count = visitors.count + 1
            RETURNING count
        ''')
        new_count = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({
            'visitors': new_count,
            'message': 'Visitor count incremented'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
