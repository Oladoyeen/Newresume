from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html")

@app.route('/submit_contact')
def submit_contact():
    return render_template("submitForm.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
