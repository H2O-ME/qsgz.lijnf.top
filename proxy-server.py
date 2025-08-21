#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SiliconFlow API 代理服务器
解决浏览器CORS跨域问题
"""

import http.server
import socketserver
import json
import urllib.request
import urllib.parse
from urllib.error import HTTPError, URLError
import sys
from http.server import BaseHTTPRequestHandler

class CORSRequestHandler(BaseHTTPRequestHandler):
    def _set_cors_headers(self):
        """设置CORS头部"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Access-Control-Max-Age', '86400')
    
    def do_OPTIONS(self):
        """处理预检请求"""
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()
    
    def do_POST(self):
        """处理POST请求"""
        if self.path == '/api/chat':
            try:
                # 读取请求体
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                request_data = json.loads(post_data.decode('utf-8'))
                
                # 构建发送到SiliconFlow的请求
                api_url = 'https://api.siliconflow.cn/v1/chat/completions'
                api_key = request_data.get('api_key', '')
                
                # 移除api_key字段，避免发送到API
                if 'api_key' in request_data:
                    del request_data['api_key']
                
                # 创建请求
                req = urllib.request.Request(
                    api_url,
                    data=json.dumps(request_data).encode('utf-8'),
                    headers={
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {api_key}'
                    }
                )
                
                # 发送请求
                with urllib.request.urlopen(req, timeout=30) as response:
                    response_data = response.read().decode('utf-8')
                    
                    # 返回成功响应
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self._set_cors_headers()
                    self.end_headers()
                    self.wfile.write(response_data.encode('utf-8'))
                    
            except HTTPError as e:
                # API错误
                error_response = {
                    'error': {
                        'message': f'API请求失败: {e.code} {e.reason}',
                        'code': e.code
                    }
                }
                self.send_response(e.code)
                self.send_header('Content-Type', 'application/json')
                self._set_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps(error_response).encode('utf-8'))
                
            except URLError as e:
                # 网络错误
                error_response = {
                    'error': {
                        'message': f'网络连接失败: {str(e)}',
                        'code': 'NETWORK_ERROR'
                    }
                }
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self._set_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps(error_response).encode('utf-8'))
                
            except Exception as e:
                # 其他错误
                error_response = {
                    'error': {
                        'message': f'服务器内部错误: {str(e)}',
                        'code': 'INTERNAL_ERROR'
                    }
                }
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self._set_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps(error_response).encode('utf-8'))
        else:
            # 404错误
            self.send_response(404)
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(b'Not Found')
    
    def log_message(self, format, *args):
        """自定义日志格式"""
        print(f"[代理服务器] {self.address_string()} - {format % args}")

def run_proxy_server(port=3001):
    """启动代理服务器"""
    try:
        with socketserver.TCPServer(("", port), CORSRequestHandler) as httpd:
            print(f"🚀 SiliconFlow API 代理服务器已启动")
            print(f"📡 监听端口: {port}")
            print(f"🌐 代理地址: http://localhost:{port}/api/chat")
            print(f"💡 使用说明: 将前端API请求发送到此地址即可解决CORS问题")
            print(f"⚠️  按 Ctrl+C 停止服务器")
            print("-" * 50)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 代理服务器已停止")
    except Exception as e:
        print(f"❌ 启动代理服务器失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 检查端口参数
    port = 3001
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ 端口号必须是数字")
            sys.exit(1)
    
    run_proxy_server(port)