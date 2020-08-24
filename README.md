# PythonTextPortal

Python scripts using Twilio for SMS integration.

### messaging_service.py

Messaging service class the loads config.json to initiate client and send SMS messages using Twilio.

### check_ip.py

Check the machine's external IP using Amazon AWS. 
Saves the IP and checks the current IP when run. If the current IP is different than the saved IP, send an SMS with the new IP.
