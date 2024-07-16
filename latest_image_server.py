import os
import signal
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import webbrowser
import json

class LatestImageHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/latestImage':
            latest_image = self.get_latest_image()
            if latest_image:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(latest_image.encode())
            else:
                self.send_response(404)
                self.end_headers()
        elif self.path == '/imageList':
            images = self.get_image_list()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(images).encode())
        elif self.path.startswith('/getImage'):
            image_name = self.path.split('=')[1]
            if os.path.exists(image_name):
                self.send_response(200)
                self.send_header('Content-type', 'image/jpeg')
                self.end_headers()
                with open(image_name, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_response(404)
                self.end_headers()
        elif self.path == '/stopServer':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            threading.Thread(target=stop_server).start()
        else:
            super().do_GET()

    def get_latest_image(self):
        images = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if not images:
            return None
        latest_image = max(images, key=os.path.getmtime)
        return latest_image

    def get_image_list(self):
        images = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        images.sort(key=os.path.getmtime, reverse=True)
        return images

def run(server_class=HTTPServer, handler_class=LatestImageHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    threading.Thread(target=open_browser).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print('Server stopped.')

def open_browser():
    webbrowser.open('http://localhost:8000')

def stop_server():
    os.kill(os.getpid(), signal.SIGTERM)

if __name__ == '__main__':
    run()

