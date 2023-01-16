#libraries to connect to the API and for the web application
from . import picture
from flask import render_template, request, current_app
import requests
from requests.auth import HTTPDigestAuth

#Image processing libraries
import PIL.Image as Image
import io
from io import BytesIO
import os 
from datetime import datetime    

#Route that receives a post method to take a snapshot and save it inside a folder with the time and date it was taken
@picture.route('/picture', methods=['GET','POST'])
def pictures():
    
    if request.method == 'GET':
        return render_template('picture.html')
    
    if request.form['submit_button']:
        
        #Digest Authentication
        auth = HTTPDigestAuth('test','test$2022')
        
        #Request to get a snapshot
        photo = requests.get('http://elipgomexico.ddns.net:1938/cgi-bin/snapshot.cgi',
        auth=auth)
        
        now = datetime.now()

        img = Image.open(BytesIO(photo.content), mode='r')
        img.save(f'application/static/IMG/{now}.jpg') 

        ImgFolder= os.path.join('static', 'IMG')
        current_app.config['UPLOAD_FOLDER'] = ImgFolder
        ImgSecurity= os.path.join(current_app.config['UPLOAD_FOLDER'], f'{now}.jpg')

        return render_template('picture.html', photo=ImgSecurity)
    else:
        return render_template('picture.html')

