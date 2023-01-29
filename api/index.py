
#from flask import Flask
from flask import Flask, render_template
#, jsonify
#import gdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if "__name__" == "__main__":
    app.run(debug=True)
    

@app.route('/about')
#def about():
 #   return 'About'

    



