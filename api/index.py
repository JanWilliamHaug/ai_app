
#from flask import Flask
from flask import Flask
#, jsonify
#import gdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if "__name__" == "__main__":
    app.run(debug=True)
    
#def home():
    #return 'Hello, World!'
    #gdown.download('https://drive.google.com/drive/folders/1UG3LP3mwzoCUcsWmXQ2TMPOp91tJ_dnt', 'colab.ipynb', quiet=False)
    #return jsonify(message='colab notebook ran successfully')

@app.route('/about')
#def about():
 #   return 'About'

"""
from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return "Hello, World!"
    gdown.download('https://drive.google.com/drive/folders/1UG3LP3mwzoCUcsWmXQ2TMPOp91tJ_dnt', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
"""
