from messaging_service import MessagingService
import urllib
import json
import re
import os

# using AWS's simple IP checker since it accepts python's default user agent header
CHECK_IP_URL = 'http://checkip.amazonaws.com'

# save file path
SAVE_FILE = './ip_save_file.json'

# initiate messaging service
messager = MessagingService('./config.json', "check_ip")

# get old IP address (if any)
old_ip = None
if os.path.isfile(SAVE_FILE):
    try:
        # open and parse old IP file
        with open(SAVE_FILE) as save_file:
            save = json.load(save_file)
            old_ip = save.get('ip')
    except:
        # send error
        messager.send_error("Unable to open and parse IP save file.")

external_ip = None
try:
    # get response
    response = urllib.request.urlopen(CHECK_IP_URL).read()

    # parse ip from response
    external_ip = response.decode('utf8').rstrip()

except:
    #send error
    messager.send_error("Finding and parsing of external IP address failed.")

 # pattern to match IP addresses
ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
if external_ip is not None and ip_pattern.match(external_ip):

    # check if IP is new
    if old_ip is None or old_ip != external_ip:

        # send IP
        messager.send("New External IP detected: " + external_ip)

        try:
            # write file
            with open(SAVE_FILE, 'w') as save_file:
                save_file.write('{"ip":"' + external_ip + '"}')

        except:
            # send error
            messager.send_error("Failed to write new IP save file.")
else:
    # send error
    messager.send_error("Parsed a malformed IP.")
