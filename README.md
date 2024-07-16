# latestImage: A simple image server in python

## Motivation
I have been messing with image generation on my local machine a lot, and sometimes I run many generations at a time. I wanted a simple, automatically updating preview of that the images for my secondary monitor. This solution was the easiest.
## Method
The ```latest_image_server.py``` and ```index.html``` files are placed in the output folder where images are stored when generated. The server simply serves the simple page the most recent image file in the directory (support for .png, .jpg, at the moment.)
## Use
### Requires Python 3 to use, and a browser that supports javascript
Place the files from the repository directly into your outputs folder (e.g. stable-diffusion-webui/outputs/[date] or ComfyUI/outputs) and then run the server by using ```python latest_image_server.py``` or try the batch file or bash script for your distribution. A browser window should open automatically, if it doesn't, simply navigate a browser to ```http://localhost:8000``` or ```http://127.0.0.1:8000``` once the server is running. Pressing the 'Stop Server' button will close the browser tab and stop the servers execution for you.
