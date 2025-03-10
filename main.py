from m5stack import *
from m5ui import *
from uiflow import *
import network
import bluetooth
import time
import machine

# Set screen background color
setScreenColor(0x222222)

# UI Elements
menu_title = M5TextBox(50, 5, "Red Team Tool", lcd.FONT_DejaVu24, 0xFF0000, rotate=0)
menu_items = ["Wi-Fi Scan", "BLE Scan", "BadUSB Attack"]
selected_index = 0
menu_text = M5TextBox(20, 50, menu_items[selected_index], lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
status_label = M5TextBox(10, 200, "Status: Ready", lcd.FONT_Default, 0x00FF00, rotate=0)

# Wi-Fi Setup
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# BLE Setup
ble = bluetooth.BLE()
ble.active(True)

# Navigation Functions
def update_menu():
    menu_text.setText(f"> {menu_items[selected_index]}")

def buttonB_wasPressed():  # Scroll menu
    global selected_index
    selected_index = (selected_index + 1) % len(menu_items)
    update_menu()

def buttonA_wasPressed():  # Select menu option
    global selected_index
    status_label.setText("Status: Working...")
    if selected_index == 0:
        wifi_scan()
    elif selected_index == 1:
        ble_scan()
    elif selected_index == 2:
        badusb_attack()
    status_label.setText("Status: Ready")

def wifi_scan():
    status_label.setText("Wi-Fi: Scanning...")
    print("[*] Scanning for Wi-Fi networks...")
    networks = wifi.scan()
    result = "\n".join([f"{net[0].decode()} ({net[3]}dBm)" for net in networks])
    menu_text.setText(result[:100])  # Show part of the result
    status_label.setText("Status: Done")

def ble_scan():
    status_label.setText("BLE: Scanning...")
    print("[*] Scanning for BLE devices...")
    ble.gap_scan(5000, 30000, 30000)
    status_label.setText("Status: Done")

def badusb_attack():
    status_label.setText("BadUSB: Executing...")
    print("[*] Injecting Rick Roll payload...")
    hid_payload = """
    DELAY 500
    GUI r
    DELAY 500
    STRING https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ENTER
    """
    print(hid_payload)  # Simulating payload execution
    status_label.setText("Status: Done")

# Bind button actions
btnA.wasPressed(buttonA_wasPressed)
btnB.wasPressed(buttonB_wasPressed)

# Initial UI update
update_menu()

# Keep program running
while True:
    wait(0.1)
