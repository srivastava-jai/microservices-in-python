from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

#function to fetch hostname and ip address
def fetchdetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello Jai Srivastava!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, ip = fetchdetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)