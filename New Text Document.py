
from gg import Tele
import jsonify
from flask import Flask, request

app = Flask(__name__)

@app.route('/chk/<name>', methods=['GET'])
def vbv(name):
  gg = str(Tele(name))
  return gg

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000)
