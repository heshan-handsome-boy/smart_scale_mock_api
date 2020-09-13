import os
import time

from flask import Blueprint, jsonify, request

garbage_blue_print = Blueprint('garbage', __name__,
                               url_prefix='/garbage',
                               static_folder='static'
                               )


@garbage_blue_print.route('/intelligentScale/khyz', methods=['POST', 'GET'])
def yz():
    card_num = request.json.get('card_num')
    imei = request.json.get('IMEI')
    print('card_num:{}'.format(card_num))
    print('imei:{}'.format(imei))
    if None in {card_num, imei}:
        return jsonify(
            {'code': 0}
        )
    time.sleep(2)
    return jsonify({
        'code': 1,
        'access_token': 12345678,
        'owner_name': '我是大帅哥',
        'garbage_type': '厨余垃圾'
    })


@garbage_blue_print.route('/intelligentScale/sjsb', methods=['POST'])
def xl():
    basedir = os.path.abspath(os.path.dirname(__file__))
    access_token = request.values.get('access_token')
    card_num = request.values.get('card_num')
    imei = request.values.get('IMEI')
    photo = request.files.get('photo')
    weight = request.values.get('weight')
    btn_result = request.values.get('btn_result')
    if None in {access_token, card_num, imei, photo, weight, btn_result}:
        return jsonify({
            'code': 0,
            'msg': '错误信息'
        })

    time.sleep(2)
    path = basedir + "/static/photo/"
    file_path = path + photo.filename
    photo.save(file_path)

    return jsonify({
        'code': 1,
        'msg': '上传成功'
    })
