from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    # request successful and you'll get your response
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message="Hello Python course d10"
    self.wfile.write(message.encode())
    return
