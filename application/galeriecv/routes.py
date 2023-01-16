#libraries to connect to the API and for the web application
from . import galeriecv
from flask import render_template, request, current_app
import requests
from requests.auth import HTTPDigestAuth
import os 

#Computer vision libraries
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt                              


#Route that processes the images taken and identifies people and objects
@galeriecv.route('/galeriecv', methods=['GET'])
def galeriecv():
    if request.method == 'GET':
        
        c=0
        ImgPerson = []

        ImgFolder= os.path.join('static', 'IMG')
        current_app.config['UPLOAD_FOLDER'] = ImgFolder
        ImgList = os.listdir('application/static/IMG')
        ImgList = ['IMG/' + i for i in ImgList]

        #Image processing
        for i in ImgList:
            c+=1
            image = cv2.imread(f'/home/kyuby/Desktop/Elipgo/application/static/{i}')
            box,label,c_score = cv.detect_common_objects(image)
            output = draw_bbox(image,box,label,c_score)
            plt.imsave(f'/home/kyuby/Desktop/Elipgo/application/static/CV/identify{c}.jpg',output)
            
            if label.count('person') >= 1:
                ImgPerson.append(f'static/CV/identify{c}.jpg')
            
            plt.ioff()

        ImgFolder= os.path.join('static', 'CV')
        current_app.config['UPLOAD_FOLDER'] = ImgFolder
        ImgList = os.listdir('application/static/CV')
        ImgList = ['CV/' + i for i in ImgList]

        return render_template('galeriecv.html', image=ImgList, imgperson=ImgPerson)

