import platform
import distro
import socket
import cpuinfo
import GPUtil
import psutil , sys
import tkinter as tk
from time import sleep

def os_info():
    root = tk.Tk()
    root.title("Device Information")
    root.columnconfigure(0, weight=1)

    # Set font style and size
    font = ("Helvetica", 20, "bold")


    # cpu model
    cpu_info = cpuinfo.get_cpu_info()
    model = cpu_info['brand_raw']

    # os of the system
    system = platform.system()
    if system == 'Windows':
        release = platform.release()
        version = platform.version()
    elif system == 'Linux':
        distro_info = distro.linux_distribution()
        release = distro_info[0]
        version = distro_info[1]
    else:
        release = 'Unknown'
        version = ''

    # ram
    total_ram = psutil.virtual_memory().total
    manufacturer=""
    # graphics card information
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        if gpu.name.lower().startswith('nvidia'):
            manufacturer = 'NVIDIA'
        elif gpu.name.lower().startswith('amd'):
            manufacturer = 'AMD'
        else:
            manufacturer = 'Unknown'
        gpu_model = gpu.name
        memory = gpu.memoryTotal

    total_storage = psutil.disk_usage('/').total



    # Create labels
    tk.Label(root, text=f"Device Name:", font=font).grid(row=0, column=0, sticky="W")
    tk.Label(root, text=f"{socket.gethostname()}", font=font).grid(row=0, column=1, sticky="W")
    tk.Label(root, text=f"CPU Model:", font=font).grid(row=1, column=0, sticky="W")
    tk.Label(root, text=f"{model}", font=font).grid(row=1, column=1, sticky="W")
    tk.Label(root, text=f"Operating System:", font=font).grid(row=2, column=0, sticky="W")
    tk.Label(root, text=f"{system} {platform.release()}", font=font).grid(row=2, column=1, sticky="W")
    tk.Label(root, text=f"", font=font).grid(row=3, column=0, sticky="W")
    tk.Label(root, text=f"{release} {version}", font=font).grid(row=3, column=1, sticky="W")
    tk.Label(root, text=f"CPU architecture:", font=font).grid(row=4, column=0, sticky="W")
    tk.Label(root, text=f"{platform.machine()}", font=font).grid(row=4, column=1, sticky="W")
    tk.Label(root, text=f"Total RAM:", font=font).grid(row=5, column=0, sticky="W")
    tk.Label(root, text=f"{total_ram / (1024 * 1024):.2f} MB", font=font).grid(row=5, column=1, sticky="W")
    tk.Label(root, text=f"Graphics Card:", font=font).grid(row=6, column=0, sticky="W")
    tk.Label(root, text=f"{manufacturer}", font=font).grid(row=6, column=1, sticky="W")
    tk.Label(root, text=f"{gpu_model}", font=font).grid(row=7, column=1, sticky="W")

    root.mainloop()