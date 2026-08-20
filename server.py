from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8000

print("REIN ViPlex server")
print("Serving on http://%s:%s" % (HOST, PORT))
print("Use your PC LAN IP in ViPlex, for example: http://192.168.1.20:%s" % PORT)
ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler).serve_forever()
