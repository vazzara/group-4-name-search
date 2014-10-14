from flask import Flask, render_template, request
import utils
import namesearch
# app is an instance of the Flask class

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def main():
    if request.method=="GET":
        return render_template("home.html")
    else:
        search = request.form['search']
        button = request.form['b']
        if (button == "Clear" or search == None):
            return render_template("home.html")
        else:
            results = namesearch.get_analysis(search)
            keys = results.keys()
            values = results.values()
            return render_template("results.html", keys=keys, values=values, search=search)

@app.route("/results")
def results():
    return render_template("results.html")

if __name__=="__main__":
# set the instance variable debug to True
    app.debug = True
# call the run method
    app.run()
