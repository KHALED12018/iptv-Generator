import random
import string
import tkinter as tk

def generate_IPTV_server(server_name):
    ip_address = "192.168.0.1"
    port = 8000

    # Generate random server ID
    server_id = random.randint(1000, 9999)

    # Generate random username and password
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

    # Format the server details
    server_details = f"Server Name: {server_name}\n"
    server_details += f"Server ID: {server_id}\n"
    server_details += f"IP Address: {ip_address}\n"
    server_details += f"Port: {port}\n"
    server_details += f"Username: {username}\n"
    server_details += f"Password: {password}\n"

    return server_details

def generate_iptv():
    server_name = entry_server_name.get()
    iptv_server = generate_IPTV_server(server_name)
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, iptv_server)

# Create the Tkinter window
window = tk.Tk()
window.title("IPTV Generator")

# Create input field for server name
label_server_name = tk.Label(window, text="Enter server name:")
label_server_name.pack()
entry_server_name = tk.Entry(window)
entry_server_name.pack()

# Create button to generate IPTV
button_generate = tk.Button(window, text="Generate IPTV", command=generate_iptv)
button_generate.pack()

# Create output field for IPTV details
text_output = tk.Text(window, height=10, width=50)
text_output.pack()

# Start the Tkinter event loop
window.mainloop()
