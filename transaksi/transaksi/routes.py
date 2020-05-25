from flask import request, jsonify, redirect, url_for
from transaksi import app
from transaksi import db
from transaksi.model import Transaksi


@app.route('/post>', methods=['POST'])
def create_post():
    new_post = Transaksi(
        status = status()
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message' : 'new posting'})

def status():
    if not status :
        return ({'belum membayar'})

    if status == 1 :
        return ({'sudah membayar'})