from flask import Flask, render_template, request
from avatars import avatar
import os
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/submit', methods=['POST'])
def submit():
    prompts = ""
    if request.form['dimension']:
        prompts = request.form['dimension']
    
    if request.form['animal']:
        prompts += request.form['animal'] + " Avatar"    
    if request.form['cap']:
        prompts += "with "+request.form['cap']
    if request.form['jwellery']:
        prompts += ", "+request.form['jwellery']
    if request.form['goggles']:
        prompts += ", "+request.form['goggles']
    if request.form['dress']:
        prompts += "wearing "+request.form['dress']
    if request.form['mood']:
        prompts += "in "+request.form['dress']+" mood"
    img_data = avatar(prompts)
    img = img_data.content
    #img = Image.open(BytesIO(content))
    return img
    # Display or save the image
    # img.show()


@app.route('/mint',methods=['POST'])
def mint_now():
    img_url = request.form['img']
    # function to do further process of minting
    return img_url
