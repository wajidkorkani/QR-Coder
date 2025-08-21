from flask import Flask, render_template as render
from flask_sqlalchemy import SQLAlchemy as sql


# Initialize Flask app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = sql(app)



# Home route
@app.route("/")
def home():
    return render("index.html")

# About route
@app.route("/about")
def about():
    return render("about.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
