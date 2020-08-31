from messaging_service import MessagingService
import requests
import json

# path to websites JSON file
WEBSITES_FILE = './websites.json'

# initiate messaging service
messager = MessagingService('./config.json', "check_websites")

# will be populated by parsing websites JSON file
urls = []

# open and parse websites JSON file to get URLs array
try:
    with open(WEBSITES_FILE) as websites_file:
        urls = json.load(websites_file).get("urls")
except:
    messager.send_error("Failed to open and parse website URLs file.")

for url in urls:

    # ping URL to get response
    try:
        response = requests.get(url)
        status = response.status_code
        if status != 200:
            messager.send("Warning! Received status code " + str(status) + " from URL " + url)
    except:
        messager.send_error("Failed to connect to " + url)
