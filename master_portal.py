import socket

print("IP of slave: ")
HOST = input()  # Replace with the IP address of your Debian VM
PORT = 12345           # The same port as used by the slave_portal.py script

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected to the Debian VM's portal.")

        while True:
            command = input("Enter a command to send to the VM (or 'exit' to quit): ")
            if command.lower() == 'exit':
                break
            s.sendall(command.encode('utf-8'))
            response = s.recv(4096).decode('utf-8')
            print(f"Response from VM:\n{response}")

if __name__ == "__main__":
    main()