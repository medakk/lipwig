# lipwig
`lipwig` lets you access your clipboard over a server. This provides a simple way of sharing text from a mobile device to the PC/laptop. `lipwig` is implemented in Python 3, and uses the `http.server` module for hosting the server.

### Usage

    ./lipwig.py [port number]
Now, browse to wherever `lipwig` is hosted:

    192.168.1.104:4321/copy
<img src="https://raw.githubusercontent.com/medakk/lipwig/master/readme_imgs/img1.png" alt="Sample image for copy" width=25% height=25%/>

To view the clipboard, navigate to:

    192.168.1.104:4321/clipboard
<img src="https://raw.githubusercontent.com/medakk/lipwig/master/readme_imgs/img2.png" alt="Sample image for clipboard" width=25% height=25%/>
