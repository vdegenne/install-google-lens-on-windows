# install-google-lens-on-windows

is a desperate attempt to have a global access to google lens anywhere on your desktop, that is crop an area of your screen and it will get loaded inside Google Lens.
My program is not pirating Google Lens original program in any means illegal.
Basically here are the linear steps executed to get the intended result :

- Trigger Windows screenshot manager
- (The user crop an area, the area is injected into the clipboard) open a new chrome window
- paste the image from the clipboard
- right click to open the Chrome contextual menu on that image
- click on "Search images with Google Lens" item


## Installation

- Install `Chrome`, `AutoHotKey`, `NodeJs` (with `npm`)
- Click `RUN.bat` (this will run the server used to paste images in the browser)
- Click on `lens-clicker.ahk`

- Now you can use <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd> to take a partial screenshot and analyse the content in *Google Lens*

**Note** : Because my computer is different from yours (screen resolution, Chrome version, etc...) You will probably need to alter some location values in the `.ahk` file. Make few testing and tweak the values to suit environment.


## Help

Any help to improve this or make it multi-platform would be much appreciated !