## How to use ?

- Install `python3`
- Install the python modules `pytesseract` and `pyautogui` (using pip)

(note: on Windows you have to also install the tesseract OCR (https://github.com/UB-Mannheim/tesseract/wiki) and add the installation location into the Windows environmental variables `PATH` (for me it was `C:\Program Files\Tesseract-OCR`))

- Alter `pytesseract.py` original script (located in `C:\Users\username\AppData\Local\Programs\Python\Python36\Lib\site-packages\pytesseract\` on Windows)
In `get_tesseract_version()` method there is `subprocess.check_output` function.
I had to add `shell=True` in the arguments list to prevent tesseract from opening a console (even if `pythonw` was used I still had a flashing console appearing)

- Install `AutoHotKey`  and run `lens-clicker.ahk` in this project directory.

- Now <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>s</kbd> should work

## Script logic

After the keychords is pressed, the script :

- right click (where the mouse is)
- screenshot
- crop a reduced region (to avoid fullscreen scan)
- find a candidate of "Search images with Google Lens" item in the opened menu
- move the mouse to the candidate
- click the candidate

## Caveat

For now the script only works if the contextual menu in Chrome open the right side of the mouse cursor (e.g. when the mouse is not near the right side of the screen). This is because the script naively crop a predefined region on the right side of the cursor to try locate the "Search images with Google Lens" item in the menu.

## Improvements

- crop the screenshot to an even more optimal region (predict the contextual menu location from the mouse location on the screen)
- Delete the need to use `AutoHotKey` and implements a background loop in the script awaiting for the keychords to be pressed;

## Collaborate

This project is opened to PR, please feel free to participate if you like the idea behind this project and want to improve it.