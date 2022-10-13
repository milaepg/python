from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def users():
    
     print(request.form)
     name_from_form = request.form["name"]
     location_from_form = request.form["location"]
     language_from_form = request.form["language"]
     color_from_form = request.form["color"] 
     message_from_form = request.form["message"]
     
     return render_template("user.html", name_on_template=name_from_form, location_on_template=location_from_form, language_on_template = language_from_form, message_on_template=message_from_form, color_on_template=color_from_form)

if __name__ == "__main__":
     app.run(debug=True)