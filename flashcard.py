from flask import Flask,render_template,request,abort,jsonify,request,redirect,url_for
from models import db,save_db
import json
app=Flask(__name__)

@app.route("/")
def introduction():
   return render_template("welcome.html",message="This is the message from view function",name="Hare",age=11,cards=db)

@app.route("/card/<int:index>")
def card(index):
   try:
      card = db[index]
      return render_template("card.html",card=card,index=index,max_index=len(db)-1)
   except IndexError as e:
      abort(400)

@app.route("/api/card")
def api_introduction():
   return jsonify(db)

@app.route("/api/card/<int:index>")
def api_card(index):
   try:     
      return db[index]
   except IndexError as e:
      abort(400)

@app.route("/api/add_card", methods=["GET","POST"])
def api_add_card():
   if request.method =="POST":
      card = {"question":request.form["question"],
              "answer":request.form["answer"]}
      db.append(card)
      save_db()
      return redirect(url_for("card",index=len(db)-1))
   else:
      return render_template('add_card.html')

@app.route("/api/remove_card/<int:index>", methods=["GET","POST"])
def api_remove_card(index):
   if request.method =="POST":
      db.pop(index)
      save_db()
      return redirect(url_for("introduction"))
   else:
      card = db[index]
      return render_template('remove_card.html',card=card)

if __name__=="__main__":
   app.run(debug=True)