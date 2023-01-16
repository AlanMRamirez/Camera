from . import home
from flask import render_template, request
import requests
from requests.auth import HTTPDigestAuth

#Root path that returns general and specific information about the camera's hardware and software
@home.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        #Digest Authentication
        auth = HTTPDigestAuth('test','test$2022')

        #Request to get the general information of the camera
        data = requests.get('http://elipgomexico.ddns.net:1938/cgi-bin/configManager.cgi?action=getConfig&name=General',
        auth=auth)

        #Request to get the machine name
        NameMachine = requests.get('http://elipgomexico.ddns.net:1938/cgi-bin/magicBox.cgi?action=getMachineName',
        auth=auth)

        #Request to get device type
        DeviceType = requests.get('http://elipgomexico.ddns.net:1938/cgi-bin/magicBox.cgi?action=getSystemInfo',
        auth=auth)

        #Request to get the serial number
        NoSerial = requests.get('http://elipgomexico.ddns.net:1938/cgi-bin/magicBox.cgi?action=getSerialNo',
        auth=auth)

        #Request to get the languages
        Languages = requests.get('http://elipgomexico.ddns.net:1938/cgi-bin/magicBox.cgi?action=getLanguageCaps',
        auth=auth)

        data = data.text.split("\r\n")
        NameMachine = NameMachine.text
        DeviceType = DeviceType.text.split("\r\n")
        NoSerial = NoSerial.text
        Languages = Languages.text


        return render_template('index.html', data=data, serial=NoSerial, name=NameMachine, device=DeviceType, language=Languages) 
    