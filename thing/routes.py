from flask import Flask, jsonify
from app import app
from thing.models import Thing

@app.route("/thing", methods=["POST"])
def posty():
    return Thing().pushy()