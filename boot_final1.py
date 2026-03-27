import network
import webrepl
#import webrepl_setup
# Replace with your Wi-Fi details
SSID = "APIS-PLS"
PASSWORD = "apispls@2025"
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect(SSID, PASSWORD)
while not sta_if.isconnected(): pass
print('Connected. IP:', sta_if.ifconfig()[0])
webrepl.start()
