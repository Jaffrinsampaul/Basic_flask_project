# from flask import Flask, redirect, url_for, request, render_template
#
# app = Flask(__name__)
#
#
# @app.route('/success/<name>', methods=['GET'])
# def success(name):
#     return f"welcome{name}"
#
#
# # @app.route('/login', methods=['POST', 'GET'])
# # def login():
# #     if request.method == 'POST':
# #         print(request.form)
# #         user = request.form['name']
# #         return redirect(url_for('success', name=user))
# #
# #     else:
# #         return render_template("login.html")
#
#
# # if __name__ == "__main__":
# #     app.run()
#
# """Homework"""
# """Homework"""
#
#
# @app.route("/", methods=["GET"])
# def home_page():
#     if request.method == "GET":
#         return render_template("user_dashboard.html")
#     return "Page not found"
#
#
# @app.route("/student_detail/<name>/<ages>/<regs>", methods=["GET"])
# def student_detail(name, ages, regs):
#     return f"<p>student detail:<br>Student name: {name}<br>Student ages: {ages}" \
#            f"<br>Student Register Number: {regs}</p>"
#
#
# @app.route("/school_detail/<school_name>/<sch_adr>/<school_num>", methods=["GET"])
# def school_detail(school_name, sch_adr, school_num):
#     return f"<p>School detail:<br>school name: {school_name}<br>school address: {sch_adr}" \
#            f"<br>school number: {school_num}</p>"
#
#
# @app.route("/login", methods=["POST", "GET"])
# def login_page():
#     if request.method == "POST":
#         print(request.form)
#         student = request.form["first_name"]
#         age = request.form["age"]
#         reg = request.form["reg"]
#         school = request.form["school"]
#         sch_adr = request.form["address"]
#         school_num = request.form["number"]
#
#         return redirect(url_for("student_detail", name=student, ages=age, regs=reg))
#         # return redirect(url_for("school_detail", school_name=school, sch_adr=sch_adr, school_num=school_num))
#
#     if request.method == "GET":
#         return render_template("login.html")
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
