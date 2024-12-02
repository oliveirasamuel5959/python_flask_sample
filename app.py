from flask import Flask, render_template

# create a flask istance
app = Flask(__name__)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route("/")
def index():
    name = "<strong>John</strong>"
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)