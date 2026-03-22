import network
import urequests
import machine
import os
import gc

# 1. WiFi Config
SSID = "APIS-PLS"
PASSWORD = "apispls@2025"
# The IP of your SERVER (the computer holding the new files)
SERVER_IP = "192.168.88.16" 

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print('Connecting to WiFi...')
        sta_if.connect(SSID, PASSWORD)
        import time
        for _ in range(15): # 15 second timeout
            if sta_if.isconnected(): break
            time.sleep(1)
    if sta_if.isconnected():
        print('Connected! IP:', sta_if.ifconfig()[0])
        return True
    return False

def check_for_updates():
    # MUST include http:// and the server's port (if not 80)
    BASE_URL = f"http://{SERVER_IP}:8000" 
    
    try:
        print("Checking for updates...")
        res = urequests.get(f"{BASE_URL}/version.json")
        new_version = res.json()['version']
        res.close()

        # Compare against a local version file
        current_version = "0.0"
        if "version.txt" in os.listdir():
            with open("version.txt", "r") as f:
                current_version = f.read().strip()

        if new_version != current_version:
            print(f"Updating to {new_version}...")
            update_res = urequests.get(f"{BASE_URL}/main.py")
            new_code = update_res.text
            update_res.close()

            with open("main.py", "w") as f:
                f.write(new_code)
            with open("version.txt", "w") as f:
                f.write(new_version)
                
            print("Update applied. Rebooting...")
            machine.reset() 
    except Exception as e:
        print("OTA Update skipped/failed:", e)
    finally:
        gc.collect()

# Run the boot sequence
if connect_wifi():
    check_for_updates()
