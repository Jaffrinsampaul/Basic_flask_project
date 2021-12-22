from flask import Flask, request, render_template, url_for, session
from werkzeug.utils import redirect
import pymongo
import random
import requests
from datetime import datetime

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# connection string
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

database = client["login_detail"]
notepad = client["notepad"]

collection = database.clientlogin_detail
notepad_collection = notepad.notepad_detail

random_number = [i for i in range(10)]


@app.route("/", methods=["GET"])
def home_page():
    if "user_name" in session:
        if session["user_name"] == "admin":
            return render_template("admin_page.html")
        if session["user_name"] != "admin":
            query_user_detail = {
                "user Name": session["user_name"]
            }
            query_notepad = {
                "user name": session["user_name"]
            }

            user_detail = collection.find_one(query_user_detail)
            notepad_db = notepad_collection.find_one(query_notepad)

            session["city_name"] = user_detail.get("recent_search_city_name")
            session["notepad_details"] = notepad_db.get("notepad")
            # print(session["notepad_details"])
            #
            if session["city_name"] is None and session["user_name"]:
                session["city_name"] = "please select city"
                session["notepad_details"] = "No Details Found"

            return render_template("user_dashboard.html")
    return render_template("landing_page.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session["login_error"] = 0
    if request.method == "POST":
        session["user_name"] = request.form["name"]
        session["password"] = request.form["password"]

        if len(session["user_name"]) != 0 and len(session["password"]) != 0:

            query = {
                "user Name": session["user_name"]
            }
            user_mongodb = collection.find_one(query)

            if user_mongodb.get("user Name") == session["user_name"] and user_mongodb.get("password") == \
                    session["password"]:
                return redirect(url_for("home_page"))
            else:
                return render_template("login.html")
        return render_template("login.html")

    if request.method == "GET":
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("home_page"))


@app.route("/new_login", methods=["POST", "GET"])
def new_login():
    if request.method == "POST":
        session["user_name"] = request.form["name"]
        session["password"] = request.form["password"]

        if len(session["user_name"]) != 0 and len(session["password"]) != 0:
            record = {

                "_id": f"{session['user_name']}_{random.choice(random_number)}",
                "user Name": session["user_name"],
                "password": session["password"]

            }
            collection.insert_one(record)
            return redirect(url_for("home_page"))
        return render_template("new_login.html")
    else:
        return render_template("new_login.html")


@app.route("/edit_page", methods=["GET", "POST"])
def edit_user_detail():
    if request.method == "POST":
        session["edit_user_name"] = request.form["edit_user_name"]
        session["edit_password"] = request.form["edit_password"]

        collection.update_one({"user Name": f'{session["user_name"]}'},
                              {"$set": {"user Name": session["edit_user_name"],
                                        "password": session["edit_password"]}})

        return render_template("user_dashboard.html")

    elif request.method == "GET":
        query_user_detail = {
            "user Name": session["user_name"]
        }

        user_detail = collection.find_one(query_user_detail)
        user_name = user_detail.get("user Name")
        user_password = user_detail.get("password")

        return render_template("edit_user.html", user_Name=user_name, pasword=user_password)


@app.route("/weather", methods=["GET", "POST"])
def get_weather():
    if request.method == "GET":
        return render_template("weather.html")
    elif request.method == "POST":
        session["city_name"] = request.form["city_name"]

        if session["city_name"] == "":
            return render_template("weather.html")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={session['city_name']}" \
              f"&appid={'f9b70b38818864f2dd4947c31b30eb65'}"

        response = requests.get(url.format(session["city_name"])).json()

        session["temp"] = response["main"]["temp"]
        session['weather_city'] = response["weather"][0]["description"]
        session['min_temp'] = response['main']['temp_min']
        session['max_temp'] = response['main']['temp_max']
        session['icon'] = response['weather'][0]['icon']

        collection.update_one({"user Name": f"{session['user_name']}"}, {"$set":
                              {"recent_search_city_name": session["city_name"]}})

        return render_template("weather.html")


@app.route("/notepad", methods=["GET", "POST"])
def notepad():
    if request.method == "GET":
        return render_template("notepad.html")
    else:
        session["notepad"] = request.form["notepad"]
        length_notepad_collection = notepad_collection.find()
        length_notepad = len(list(length_notepad_collection))
        id_number = length_notepad + 1
        print(id_number)

        created_date_time = datetime.now()

        if length_notepad == 0:
            convert_dict = {
                "_id": 1,
                "user name": session["user_name"],
                "notepad": session["notepad"],
                "created date": created_date_time.strftime("%d%m%y %H:%M")
            }
            notepad_collection.insert_one(convert_dict)
            return render_template("notepad.html")

        else:
            convert_dict = {
                "_id": id_number,
                "user name": session["user_name"],
                "notepad": session["notepad"],
                "created date": created_date_time.strftime("%d/%m/%y %H:%M")
            }
            notepad_collection.insert_one(convert_dict)
            return render_template("notepad.html")


if __name__ == "__main__":
    app.run(debug=True)
