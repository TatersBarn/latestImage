import os
import signal
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import webbrowser

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
        elif self.path == '/stopServer':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            threading.Thread(target=stop_server).start()
        else:
            super().do_GET()  # Serve files as usual

    def get_latest_image(self):
        images = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if not images:
            return None
        latest_image = max(images, key=os.path.getmtime)
        return latest_image

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

