# coding=utf-8
import urllib.request
import base64
import json

def accessToken():

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=VAph9s6xAxuqGeziq7ZcCczi&client_secret=NVfV3Y1fFzhK1S8nFQwwAnfEsbvoRedE'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    return response.read()
print(accessToken())

def faceContrast(imageFile,imageUrl):
    '''
    人脸对比
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

    image = base64.b64encode(imageFile)

    params = json.dumps(
        [{"image": image, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
         {"image": imageUrl, "image_type": "URL", "face_type": "LIVE", "quality_control": "LOW"}])

    access_token = accessToken.get('access_token')
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        print
        content