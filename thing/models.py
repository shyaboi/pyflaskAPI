from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
import uuid
from app import db

class Thing:

    def pushy(self):
#object model 
      thing = {
        "_id":uuid.uuid4().hex,
        "name":request.form.get('name'),
        "thing":request.form.get('thing'),
        "pass":request.form.get('pass')

    }

      thing["pass"] = pbkdf2_sha256.encrypt(thing['pass'])
      print(request.form)

      db.thing.insert_one(thing)
      return jsonify(thing),200
