# CustomFirmware
Firmware for M5Stick-CPlus 1.1 

## Menu System
The firmware includes a menu system with the following options:
- Wi-Fi Scan
- BLE Scan
- BadUSB Attack

The menu system is implemented using `menu_items` and `selected_index` variables. The `buttonB_wasPressed` function handles scrolling through the menu options, and the `buttonA_wasPressed` function handles selecting the menu option and executing the corresponding function.

## Wi-Fi and BLE Setup
The firmware sets up Wi-Fi and BLE connections using the `network` and `bluetooth` modules. The Wi-Fi setup is done using the `network.WLAN` class, and the BLE setup is done using the `bluetooth.BLE` class.

## Button Actions
The firmware binds button actions to the `btnA` and `btnB` buttons to handle navigation and selection. The `buttonB_wasPressed` function scrolls through the menu options, and the `buttonA_wasPressed` function selects the menu option and executes the corresponding function.
