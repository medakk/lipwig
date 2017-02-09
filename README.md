# lipwig
lipwig is a server that uses an endpoint to copy data to clipboard. This provides a simple way of sharing text from a mobile device to the PC/laptop. `lipwig` also allows you to view clipboard data from the PC on other devices.

`lipwig` is implemented in Python 3.

### Usage

    ./lipwig [port number]
Now, browse to wherever `lipwig` is hosted:

    192.168.1.104:4321/copy
<img src="https://raw.githubusercontent.com/medakk/lipwig/master/readme_imgs/img1.png" alt="Sample image for copy" width=25% height=25%/>

To view the clipboard, navigate to:

    192.168.1.104:4321/clipboard
<img src="https://raw.githubusercontent.com/medakk/lipwig/master/readme_imgs/img2.png" alt="Sample image for clipboard" width=25% height=25%/>
