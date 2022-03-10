import re
# from time import sleep
import pyautogui
import pytesseract
# from PIL import Image
import numpy as np
# import ctypes
# import os
# import win32process

# hwnd = ctypes.windll.kernel32.GetConsoleWindow()
# if hwnd != 0:
#   ctypes.windll.user32.ShowWindow(hwnd, 0)
#   ctypes.windll.kernel32.CloseHandle(hwnd)
#   _, pid = win32process.GetWindowThreadProcessId(hwnd)
#   os.system('taskkill /PID ' + str(pid) + ' /f')
# if hwnd != 0:
#     ctypes.windll.user32.ShowWindow(hwnd, 0)
#     ctypes.windll.kernel32.CloseHandle(hwnd)
#     _, pid = win32process.GetWindowThreadProcessId(hwnd)
#     os.system('taskkill /PID ' + str(pid) + ' /f')

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

pyautogui.rightClick()
# # Get metadata
mouse = pyautogui.position()
screenshot = pyautogui.screenshot()
# crop location
cropleft, croptop, cropright, cropbottom = mouse.x, 0, mouse.x + 250, screenshot.height
# crop the screenshot to have a reduce area to OCR and less chance to capture the wrong keywords
cropped = screenshot.crop((cropleft, croptop, cropright, cropbottom))
# Get the image data
data = pytesseract.image_to_data(cropped)
# Find the candidates (to click)
candidates = []
for line in data.splitlines():
    row = np.array(line.split('\t'))
    if (len(row) == 12 and (re.search('Lens', row[11]) or re.search('Google', row[11]) or re.search('images', row[11]) or re.search('Search', row[11]))):
      candidates.append(row)

# target location
if len(candidates) > 0:
  target = candidates[len(candidates) - 1]
  targetl,targett,targetw,targeth = map((lambda x: int(x)), target[6:10])
  targetx,targety = targetl + (targetw / 2), targett + (targeth / 2)

  # we save the last cursor position
  last_mouse_position = pyautogui.position()
  pyautogui.moveTo(cropleft + targetx, croptop + targety)
  pyautogui.click()
  pyautogui.moveTo(last_mouse_position.x, last_mouse_position.y)