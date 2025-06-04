import os
import platform
import subprocess

def get_system_uptime():
    system = platform.system()
    if system == "Windows":
        # Windows: use 'net stats srv' and parse output
        try:
            output = subprocess.check_output("net stats workstation", shell=True, text=True)
            for line in output.split('\n'):
                if "Statistics since" in line:
                    print("System uptime (since):", line.strip().split("since")[1].strip())
                    return
        except Exception as e:
            print("Error retrieving uptime on Windows:", e)
    elif system == "Linux":
        # Linux: read /proc/uptime
        try:
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.readline().split()[0])
                uptime_string = format_uptime(uptime_seconds)
                print("System uptime:", uptime_string)
        except Exception as e:
            print("Error retrieving uptime on Linux:", e)
    elif system == "Darwin":
        # macOS: use 'uptime' command
        try:
            output = subprocess.check_output("uptime", shell=True, text=True)
            print("System uptime:", output.strip())
        except Exception as e:
            print("Error retrieving uptime on macOS:", e)
    else:
        print("Unsupported operating system.")

def format_uptime(seconds):
    days = int(seconds // (24 * 3600))
    seconds %= (24 * 3600)
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == "__main__":
    get_system_uptime()
