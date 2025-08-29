
# Import necessary libraries
from flask import Flask, render_template as render, redirect, request, url_for  # Flask web framework
import qrcode  # QR code generation
import io  # In-memory streams
import os  # File and directory operations
from PIL import Image  # Image processing
from pyzbar.pyzbar import decode  # QR code decoding
import cv2  # OpenCV for camera operations
import time  # Time operations

# Initialize Flask app

# Initialize Flask app
app = Flask(__name__)


# Home page route
@app.route("/")
def home():
    return render("index.html")


# About page route
@app.route("/about")
def about():
    return render("about.html")


# QR code generation form route
@app.route("/generate")
def generate_qr():
    return render("generate.html")


# Handle QR code image generation and saving
@app.route("/genqrimage", methods=["POST"])
def generateQrImage():
    if request.method == "POST":
        text = request.form["data"]  # Get text data from form
        qr = qrcode.QRCode(
            box_size=10,
            border=4
        )
        qr.add_data(text)  # Add data to QR code
        qr.make(fit=True)
        img = qr.make_image(
            fill_color="black",
            back_color="white",
        )
        buffer = io.BytesIO()  # Create buffer for image
        img.save(buffer, format="png")
        buffer.seek(0)
        print("img generated")
        folder = "static/images"
        os.makedirs(folder, exist_ok=True)  # Ensure folder exists
        img_path = f"{folder}/qrCode.png"
        img.save(img_path)  # Save image to disk
        print("img saved")
        return render("generateQrImage.html")  # Show result page
    return redirect(url_for("home"))  # Redirect if not POST


# QR code scan page route
@app.route('/scan')
def scan():
    return render('scan.html')


# Handle uploaded image and decode QR code
@app.route('/showQRCode', methods=["POST", "GET"])
def ShowQRCode():
    print("Api got hit")
    if request.method == 'POST':
        print("It is a post request.")
        file = request.files.get('image')  # Get uploaded image
        print("File is recieved.")
        img = Image.open(file)  # Open image
        print("File is open")
        result = decode(img)  # Decode QR code from image
        print("Image has been decoded.")
        code = ""
        for qr in result:
            print("It is foreach loop")
            code = qr.data.decode("utf-8")  # Extract QR code data
            print("Code: ", code)
        return render("showQRCode.html", codeResult=code)  # Show result
    return redirect(url_for("scan"))  # Redirect if not POST



# Live QR code scan using webcam
@app.route("/live-scan")
def liveQRCodeScan():
    cap = cv2.VideoCapture(0)  # Start webcam

    if not cap.isOpened():
        return render("liveScan.html", error = "Camera not available")

    capturedImage = "image.jpg"
    startTime = time.time()
    frame = None

    while True:
        ret, frame = cap.read()  # Read frame from webcam
        if not ret:
            break

        cv2.imshow("Laptop Camera", frame)  # Show frame

        # Close after 10 seconds
        if time.time() - startTime >= 10:
            cv2.imwrite(capturedImage, frame)  # Save frame as image
            break

        # Required to keep imshow window responsive
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Make sure an image was captured
    if frame is None:
        return render("liveScan.html", error = "No frame captured")

    # Decode QR code from captured image
    image = Image.open(capturedImage)
    decoded = decode(image)

    data = ""
    for i in decoded:
        data = i.data.decode("utf-8")  # Extract QR code data

    return render("liveScan.html", data =  data)  # Show result


# Run the Flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
