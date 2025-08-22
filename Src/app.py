from flask import Flask, render_template as render, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy as sql
import qrcode
import io
import os
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
    return render("generate.html")

@app.route("/genqrimage", methods=["POST"])
def generateQrImage():
    if request.method == "POST":
        text = request.form["data"]
        qr = qrcode.QRCode(
            box_size=10,
            border=4
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(
            fill_color="white",
            back_color="black",
        )
        buffer = io.BytesIO()
        img.save(buffer, format="png")
        buffer.seek(0)
        print("img generated")
        folder = "static/images"
        os.makedirs(folder, exist_ok=True)
        img_path = f"{folder}/qrCode.png"
        img.save(img_path)
        print("img saved")
        return redirect(url_for("home"))
    return redirect(url_for("home"))
    
# Run the app
if __name__ == "__main__":
    app.run(debug=True)
