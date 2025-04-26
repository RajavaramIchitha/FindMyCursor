import pyautogui
import keyboard
import sys

def move_cursor_to_center():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.moveTo(center_x, center_y)
    print(f"Cursor moved to center: ({center_x}, {center_y})")

def exit_program():
    print("Exiting the program...")
    sys.exit()

print("Press Ctrl + Shift + M to center the cursor.")
print("Press Ctrl + Shift + Q to quit.")

# Listen for hotkeys
keyboard.add_hotkey('ctrl+shift+m', move_cursor_to_center)
keyboard.add_hotkey('ctrl+shift+q', exit_program)

# Keep the program running
keyboard.wait()
