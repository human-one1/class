import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A陳咨穎的求職網頁</h1>"
    homepage += "<a href=/aboutme>我的個人簡介</a><br>"
    homepage += "<a href=/hello>相關工作介紹</a><br>"
    homepage += "<a href=/text>職涯測驗結果</a><br>"
    homepage += "<a href=/name>求職履歷自傳</a><br>"
    homepage += "<br><a href=/read>讀取Firestore資料</a><br>"
    return homepage

@app.route("/aboutme")
def aboutme():
    now = datetime.now()
    return render_template("aboutme.html", datetime = str(now))



@app.route("/hello")
def hello():
    now = datetime.now()
    return render_template("hello.html", datetime = str(now))



@app.route("/text")
def text():
    now = datetime.now()
    return render_template("text.html", datetime = str(now))

@app.route("/name")
def name():
    now = datetime.now()
    return render_template("name.html", datetime = str(now))


@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/read")
def read():
    Result = ""     
    collection_ref = db.collection("靜宜資管")    
    docs = collection_ref.order_by("mail", direction=firestore.Query.DESCENDING).get()    
    for doc in docs:         
        Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
    return Result





#if __name__ == "__main__":
#   app.run()
