# PythonTextPortal

Python scripts using Twilio for SMS integration.

### messaging_service.py

Messaging service class the loads config.json to initiate client and send SMS messages using Twilio.
See config-example.json for an example of the messaging service config.json file.

### check_ip.py

Check the machine's external IP using Amazon AWS. 
Saves the IP and checks the current IP when run. If the current IP is different than the saved IP, send an SMS with the new IP.

### check_websites.py

Iterates through a list of URLs in websites.json pinging each one and checking for a response with a status code of 200. In the even that the script does not receive this status code or fails to connect, it will send a SMS message using messaging_service.py warning that the URL is invalid. For an example of the websites.json file, see websites-example.json.
