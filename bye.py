import http.server
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <title>Obrigado por acessar!</title>
  <style>
    :root { --bg1:#6a11cb; --bg2:#2575fc; }
    html,body{height:100%;margin:0}
    body{
      display:flex;align-items:center;justify-content:center;
      background:linear-gradient(135deg,var(--bg1),var(--bg2));
      font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Ubuntu,'Helvetica Neue',Arial,sans-serif;
      color:#fff;
    }
    .card{
      text-align:center;background:rgba(255,255,255,.1);
      padding:40px 56px;border-radius:20px;
      box-shadow:0 10px 30px rgba(0,0,0,.25);
      backdrop-filter:saturate(140%) blur(6px);
      animation:fade 600ms ease-out both;
    }
    h1{margin:0 0 8px;font-size:2.4rem}
    p{margin:0;opacity:.9}
    @keyframes fade{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
  </style>
</head>
<body>
  <div class="card">
    <h1>Obrigado por acessar!</h1>
    <p>Esperamos que você tenha uma ótima experiência.</p>
  </div>
</body>
</html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

    def log_message(self, fmt, *args):
        return  # silencia logs no terminal

def main():
    # porta 0 = escolha automática de uma porta livre
    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as httpd:
        port = httpd.server_address[1]
        url = f"http://127.0.0.1:{port}/"
        print(f"Servidor rodando em {url} (Ctrl+C para encerrar)")
        webbrowser.open(url, new=2)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
