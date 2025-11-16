from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/file/<path:filename>")
def download_file(filename):
    return send_from_directory("filesys", filename)

if __name__ == "__main__":
    app.run(debug=True)
