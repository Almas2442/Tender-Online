from flask import request, jsonify, redirect, url_for
from posting import app
from posting import db
from posting.models import Posting

import datetime

@app.route('/post/<id_profile_buyer>', methods=['POST'])
def create_post(id_profile_buyer):
    data = request.get_json()
    d = datetime.datetime.now()
    new_post = Posting(
        name_product = data['name_product'],
        brand = data['brand'],
        description = data['description'],
        id_profile_buyer = id_profile_buyer,
        tgl_buat = d
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message' : 'new posting'})

@app.route('/read/<id_profile_buyer>', methods=['POST', 'GET'])
def read_post(id_profile_buyer):
    
    post = Posting.query.filter_by(id_profile_buyer=id_profile_buyer).first()

    if not post:
        return jsonify({'message' : 'belum posting'})

    user_data = {}
    user_data['id'] = post.id
    user_data['name_product'] = post.name_product
    user_data['brand'] = post.brand
    user_data['description'] = post.description
    user_data['picture'] = post.picture

    return jsonify({'post' : user_data})