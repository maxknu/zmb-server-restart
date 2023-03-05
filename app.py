from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    query = request.form.get('password')

    print(query)
    if (query == "survive"):
        url = "http://192.168.1.18:8126/container/ProjectZomboid/restart"
        headers = { "Content-Type": "application/octet-stream; charset=utf-8" }
        response = requests.get(url, headers=headers)
        
        return render_template('index.html', result={"result": "OK - Server restarting!"})
    else:
        return render_template('index.html', result={"result": "Wrong password"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)