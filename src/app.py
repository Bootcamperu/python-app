from flask import Flask ,jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/vi/details')

def details():
       ahora = datetime.now()
       return jsonify({
        "name": "Julio Carranza",
        "age": 40,
        "city": "Lima/Peru",
         "fecha": ahora.strftime("%Y-%m-%d"),
    })



@app.route('/api/vi/healthz')
def healthz():
       ahora = datetime.now()
       return jsonify({
        "status": "up",
         "fecha": ahora.strftime("%Y-%m-%d"),

    })

if __name__ == '__main__':
    app.run(host="0.0.0.0")


   
