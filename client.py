import socket
import pyautogui
import json
from cryptography.fernet import Fernet

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.12.89", 9999)) 
    print("Connected to the server.")

    # Receive the encryption key
    key = client.recv(1024)
    cipher = Fernet(key)
    print("Received encryption key from the server.")

    # Basic authentication
    password = input("Enter password: ")
    client.send(password.encode())
    print("Sent password to the server.")
    response = client.recv(1024).decode()
    print(f"Received response from server: {response}")
    if response != "Authenticated":
        print("Authentication failed.")
        return

    print("Authenticated successfully.")
    
    # Receive the information from the server
    try:
        while True:
            encrypted_data = client.recv(1024)
            if not encrypted_data:
                break
            data = cipher.decrypt(encrypted_data).decode()
            cursor_data = json.loads(data)
            x = cursor_data["x"]
            y = cursor_data["y"]
            pyautogui.moveTo(x, y)
    except (ConnectionResetError, BrokenPipeError):
        print("Connection error with server.")
    finally:
        client.close()

if __name__ == "__main__":
    main()
