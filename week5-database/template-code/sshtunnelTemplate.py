from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    '192.168.56.102',
    ssh_username="oscar",
    ssh_password="0206",
    remote_bind_address=('127.0.0.1', 8080)
)

server.start()

print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

server.stop()
