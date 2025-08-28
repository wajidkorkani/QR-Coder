from flask import Flask, render_template as render, redirect, request, url_for
import qrcode
import io
import os
from PIL import Image
# from pyzbar.pyzbar import decode
from pyzbar.pyzbar import decode
import cv2
import time

# Initialize Flask app
app = Flask(__name__)

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
            fill_color="black",
            back_color="white",
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
        return render("generateQrImage.html")
    return redirect(url_for("home"))

@app.route('/scan')
def scan():
    return render('scan.html')

@app.route('/showQRCode', methods=["POST", "GET"])
def ShowQRCode():
    print("Api got hit")
    if request.method == 'POST':
        print("It is a post request.")
        file = request.files.get('image')
        print("File is recieved.")
        img = Image.open(file)
        print("File is open")
        result = decode(img)
        print("Image has been decoded.")
        code = ""
        for qr in result:
            print("It is foreach loop")
            code = qr.data.decode("utf-8")
            print("Code: ", code)
        return render("showQRCode.html", codeResult=code)
    return redirect(url_for("scan"))


@app.route("/live-scan")
def liveQRCodeScan():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return render("liveScan.html", error = "Camera not available")

    capturedImage = "image.jpg"
    startTime = time.time()
    frame = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Laptop Camera", frame)

        # Close after 10 seconds
        if time.time() - startTime >= 10:
            cv2.imwrite(capturedImage, frame)
            break

        # Required to keep imshow window responsive
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Make sure an image was captured
    if frame is None:
        return render("liveScan.html", error = "No frame captured")

    # Decode QR code
    image = Image.open(capturedImage)
    decoded = decode(image)

    data = ""
    for i in decoded:
        data = i.data.decode("utf-8")

    return render("liveScan.html", data =  data)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
