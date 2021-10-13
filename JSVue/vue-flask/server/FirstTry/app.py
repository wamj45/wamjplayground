import sys
import traceback

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


print("Chcek")

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8080)
    except Exception as e:
        print("System exception running VMLINK installer app: {}".format(str(e)))
        tb = traceback.format_exc()
        print(tb)
