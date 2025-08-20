from flask import Flask, render_template as render

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

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
