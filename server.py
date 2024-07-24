import socket
import threading
import pyautogui
import json
import time
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import scrolledtext

# Key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# GUI for server computer
class ServerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Server")
        
        self.log = scrolledtext.ScrolledText(master, state='disabled', width=50, height=20)
        self.log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.start_button = tk.Button(master, text="Start Server", command=self.start_server)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.stop_button = tk.Button(master, text="Stop Server", command=self.stop_server, state='disabled')
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)

        self.server = None
        self.running = False

    def log_message(self, message):
        self.log.config(state='normal')
        self.log.insert(tk.END, message + '\n')
        self.log.config(state='disabled')
        self.log.yview(tk.END)

    # Read cursor position from server
    def get_cursor_position(self):
        x, y = pyautogui.position()
        return {"x": x, "y": y}

    # Send messages to client
    def handle_client(self, conn):
        try:
            conn.send(key)
            self.log_message("Encryption key sent to the client.")
            
            password = conn.recv(1024).decode().strip()
            self.log_message(f"Received password from client: {password}")
            if password != "password123":
                conn.send(b"Authentication failed")
                self.log_message("Authentication failed.")
                return

            conn.send(b"Authenticated")
            self.log_message("Client authenticated successfully.")

            # Update cursor on the client's computer
            while self.running:
                cursor_data = self.get_cursor_position()
                data = json.dumps(cursor_data)
                encrypted_data = cipher.encrypt(data.encode())
                conn.send(encrypted_data)
                time.sleep(0.1)
        except (ConnectionResetError, BrokenPipeError):
            self.log_message("Connection error with client.")
        finally:
            conn.close()

    # Start the server connection
    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 9999))
        self.server.listen(5)
        self.log_message("Server listening on port 9999...")
        self.running = True
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')

        threading.Thread(target=self.accept_clients).start()

    # Stop the server connection
    def stop_server(self):
        self.running = False
        if self.server:
            self.server.close()
            self.log_message("Server stopped.")
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

    # Accepts the client's computer
    def accept_clients(self):
        while self.running:
            try:
                conn, addr = self.server.accept()
                self.log_message(f"Connected to {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(conn,))
                client_thread.start()
            except OSError:
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerGUI(root)
    root.mainloop()
