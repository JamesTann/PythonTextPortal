from urllib import request
from messaging_service import MessagingService

# using AWS's simple IP checker since it accepts python's default user agent header
CHECK_IP_URL = 'http://checkip.amazonaws.com'

# initiate messaging service
messager = MessagingService('./config.json')

try:
    # get response
    response = request.urlopen(CHECK_IP_URL).read()

    # parse ip from response
    externalip = response.decode('utf8').split("'")[0].rstrip()

    # send ip
    messager.send("External IP: " + externalip)
except:
    #send error
    messager.send("Error: Finding and parsing of external IP address failed.")
