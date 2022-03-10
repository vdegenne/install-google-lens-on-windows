;!+s::Run, pythonw "lens-clicker.pyw"
!+s::
; Trigger the "take a screenshot" (partial) on Windows
Send,	{LWin Down}S{LWin Up}
; We wait for the screenshot to be cropped
KeyWait, Lbutton, D
KeyWait, Lbutton
; Open the server page in a new Chrome window
Run, chrome.exe http://localhost:43191/ --new-window
; We Wait for the window to load completely
WinWaitActive, localhost:43191
WinMaximize
WinWaitActive, localhost:43191
; Get the position of the just opened Chrome window
;WinGetPos, X, Y, W, H, A
; Try to move the mouse to a blank space on the page (ideally the most top left corner)
; MODIFY THE NUMBERS DEPENDING ON YOUR SCREEN RESOLUTION
MouseMove, 77, 100
Send, ^v
;MouseGetPos, xpos, ypos
;MsgBox, %xpos%, %ypos%
Send, {Click Right}
; Move cursor to "Search images with Google Lens"
; MODIFY THE VALUES DEPENDING ON YOUR ENVIRONMENT
MouseMove, 40, 130, 0, R
; Then Click "Search images with Google Lens"
Send, {Click}
;WinWaitActive, Google Lens
Sleep 20
Send, ^{Tab}
Send, ^w
;WinMaximize