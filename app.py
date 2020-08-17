from flask import Flask, render_template

app = Flask(__name__)
#mongo db
import pymongo
import urllib
import urllib.parse
# client = pymongo.MongoClient('localhost', 27017)

mongo_uri = "mongodb+srv://shyaboi:" + urllib.parse.quote("Ians@1kou") + "@cluster0.zqw64.azure.mongodb.net/donu?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)


db = client.Python_Flask_API
#routes
from thing import routes

@app.route("/")
def home():

    # ok = db.thing.find()
    # for donus in ok:
    #     print(donus)
    arrs = list(db.thing.find())
    print(arrs)
    return render_template("home.html", arrs=arrs)
    
