from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#creating a route
@app.route('/')
@app.route('/home')

