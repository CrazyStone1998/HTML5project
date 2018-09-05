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

def faceContrast(imageRequest,imageDatabase):
    '''
    人脸对比
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

    imageRequest_base64 = base64.b64encode(imageRequest)
    imageDatabase_base64 = base64.b64encode(imageDatabase)

    params = json.dumps(
        [{"image": str(imageRequest_base64, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
         {"image": str(imageDatabase_base64, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"}]
    ).encode('utf-8')


    access_token = eval(str(accessToken(),encoding='utf-8'))['access_token']
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    result = {}
    content = eval(str(response.read(), encoding='utf-8'))
    if content['error_msg'] == 'SUCCESS':
        if content['result']['score'] >= 80:
            result['result'] = 'SUCCESS'
        else:
            result['result'] = 'FAILED'
            result['msg'] = 'undermatching'
    else:
        result['result'] = 'FAILED'
        result['msg'] = content['error_msg']

    return result

def facerecognize(imageRegister):
    '''
    人脸检测与属性分析
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    imageRegister_base64 = base64.b64encode(imageRegister)
    params = json.dumps(
        {"image": str(imageRegister_base64, 'utf-8'), "image_type": "BASE64","face_field": "faceshape,facetype",},
    ).encode('utf-8')
    access_token = eval(str(accessToken(),encoding='utf-8'))['access_token']
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = json.loads(str(response.read(),encoding='utf-8'))
    result = {}
    if content['error_msg'] == 'SUCCESS':
        if content['result']['face_list'][0]['face_probability'] >= 0.5:
            result['result'] = 'SUCCESS'
    else:
        result['result'] = 'FAILED'
        result['msg'] = 'Face mismatch'
    return result
