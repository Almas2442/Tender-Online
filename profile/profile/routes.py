from flask import Flask, request, jsonify, app
from profile import app
from profile.models import Profile

@app.route('/profile', methods=['POST'])
def create_profile():
    data = request.get_json()
    new_profile = Profile(
        name = data['name'], 
        address = data['address'],
        phone_number = data['phone_number'])
    
    db.session.add(new_profile)
    db.session.commit()

    return jsonify({'message' : 'New profile created!'})

@app.route('/delete/<id>', methods=['DELETE'])
def delete_profile(id):
    
    user = Profile.query.filter_by(id=id).first()
    
    if not user:
        return jsonify({'message' : 'user tidak ada'})
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message' : 'user telah di hapus'})

@app.route('/update/<id>', methods=['PUT'])
def put_profile(id):
    
    data = request.get_json()
    user = Profile.query.filter_by(id=id).first()

    if not user:
        return jsonify({'message' : 'user tidak ada'})

    Profile.name = data['nama']
    Profile.address = data['address']
    Profile.phone_number = data['phone_number']

    db.session.commit()

    return jsonify({'message' : 'data berhasil di update'})

@app.route('/read/<id>', methods=['GET','POST'])
def read_profile(id):

    user = Profile.query.filter_by(id=id).first()

    if not user:
        return jsonify({'message' : 'user tidak ada'})
    
    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['address'] = user.address
    user_data['phone_name'] = user.phone_number

    return jsonify({'user' : user_data})