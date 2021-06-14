from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/5083070470e7db605e88"
response = requests.get(url=url)
results = response.json()


@app.route("/")
def homepage():
    return render_template("index.html", posts=results)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    for result in results:
        if result["id"] == post_id:
            return render_template("post.html", post=result)


if __name__ == "__main__":
    app.run(debug=True)
