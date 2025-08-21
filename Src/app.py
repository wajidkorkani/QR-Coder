from flask import Flask, render_template as render
from flask_sqlalchemy import SQLAlchemy as sql


# Initialize Flask app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = sql(app)

class QrCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<QrCode {self.id}>"

# Home route
@app.route("/")
def home():
    return render("index.html")

# About route
@app.route("/about")
def about():
    return render("about.html")

@app.route("/generate")
def generate_qr():
    # Placeholder for QR code generation logic
    return render("generate.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
