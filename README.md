# arquive-wapp-chats

Simple Python script to arquive all WhatsApp chats and leave your inbox clear &lt;3 

## About 

All the chats will be archived. Selenium is used to reproduce the user manual action of archiving the chats.

Right now, it only works on Chrome.

## Requirements

- Google Chrome
- Python > 3.6
- Chromedriver

## Setup

### Create Chrome profile to be used

You will need to specify a Chrome profile in order for the Selenium driver to run. You can either create one or resuse. Regardless of your decision, you'll need to scan the QR code on https://web.whatsapp.com and inform the profile directory used.

### Install dependencies

`pip install -r requiments.txt`

### Fill in `settings.py`

`cp sample.settings.py settings.py`

replace `PROFILE_DIRECTORY` with your desired Chrome profile and `USER_DATA_DIR` with your dir. This is my file:

```py
USER_DATA_DIR="/Users/danielbastos/Library/Application Support/Google/Chrome/"
PROFILE_DIRECTORY="Profile 3"
```

## Running

`python3 main.py`
