import network
import socket

def setup_wifi():
  ssid, pw = open('secret').readline().strip().split(';')
  sta_if = network.WLAN(network.STA_IF)
  ap_if = network.WLAN(network.AP_IF)
  ap_if.active(False)
  sta_if.active(True)
  sta_if.scan()
  sta_if.connect(ssid, pw)
  sta_if.isconnected()
  while not sta_if.isconnected():
    pass

def readfile(fname):
  f = open(fname)
  buf_size = 4096
  buf = f.read(buf_size)
  while buf != '':
    yield buf.replace("\n", "")
    buf = f.read(buf_size)

def handle(c):
  method, url, version = c.readline().split(b" ")
  if b"?" in url:
    path, query = url.split(b"?", 2)
  else:
    path, query = url, b""
  while True:
    header = c.readline()
    if header == b"":
      return
    if header == b"\r\n":
      break

  if url != b"":
    #c.write("HTTP/1.0 200 OK\r\n")
    #c.write("Content-Type: application/octet-stream\r\n")
    #c.write("Content-Disposition: inline\r\n")
    #c.write("\r\n")
    for chunk in readfile(url[1:]):
       c.write(chunk)
    return

  c.write("<!DOCTYPE html><title>Hey Ho</title>")
  c.write("<div><p>Text Here</p></div")
  c.write(f"<div><p>{path}</p></div>")
  c.write(f"<div><p>{query}</p></div>")


def run_server():
  server = socket.socket()
  server.bind(('0.0.0.0', 80))
  server.listen(1)

  while True:
    try:
      c, addr = server.accept()
      handle(c)
    except Exception as e:
      c.write('HTTP/1.1 500 Internal Server Error\r\n\r\n')
      c.write('<h1>Internal Server Error</h1>')
      print(f"Error: {e}")
    finally:
      c.close()

setup_wifi()
run_server()
