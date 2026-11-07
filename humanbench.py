import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL("user32", use_last_error=True)
gdi32 = ctypes.WinDLL("gdi32", use_last_error=True)

# Windows API structures and function signatures
class POINT(ctypes.Structure):
    _fields_ = [
        ("x", wintypes.LONG),
        ("y", wintypes.LONG)
    ]

user32.GetCursorPos.argtypes = [ctypes.POINTER(POINT)]
user32.GetCursorPos.restype = wintypes.BOOL

user32.GetDC.argtypes = [wintypes.HWND]
user32.GetDC.restype = wintypes.HDC

gdi32.GetPixel.argtypes = [
    wintypes.HDC, ctypes.c_int, ctypes.c_int
]
gdi32.GetPixel.restype = wintypes.COLORREF

user32.mouse_event.argtypes = [
    wintypes.DWORD, wintypes.DWORD,
    wintypes.DWORD, wintypes.DWORD, 
    ctypes.c_size_t
]

# Constants
TARGET = (75, 219, 106)
LEFTDOWN = 0x0002
LEFTUP = 0x0004
CLR_INVALID = 0xFFFFFFFF

# Acquire the screen device context once
hdc = user32.GetDC(None)
if not hdc:
    raise RuntimeError("Could not acquire screen DC")

point = POINT()
already_clicked = False

try:
    while True:
        user32.GetCursorPos(ctypes.byref(point))

        pixel = gdi32.GetPixel(hdc, point.x, point.y)

        if pixel == CLR_INVALID:
            continue

        # Windows COLORREF stores RGB as 0x00BBGGRR
        color = (
            pixel & 0xFF,
            (pixel >> 8) & 0xFF,
            (pixel >> 16) & 0xFF
        )

        if color == TARGET:
            if not already_clicked:
                already_clicked = True
                user32.mouse_event(LEFTDOWN, 0, 0, 0, 0)
                user32.mouse_event(LEFTUP, 0, 0, 0, 0)
        else:
            already_clicked = False

finally:
    user32.ReleaseDC(None, hdc)
