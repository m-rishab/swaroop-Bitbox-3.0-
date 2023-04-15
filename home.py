from flask import Flask, render_template, request,redirect
from avatars import avatar
import os
from PIL import Image
from io import BytesIO
import json

app = Flask(__name__,template_folder='template')

@app.route("/")
def hello_world():
    return render_template('form.html')

@app.route('/submit', methods=['post'])
def submit():
    global pay
    pay = 0
    prompts = ""
    dim = request.form.get('dimension')
    ann = request.form.get('animal')
    cap = request.form.get('cap')
    jwellery = request.form.get('jwellery')
    goggles = request.form.get('goggles')
    dress = request.form.get('dress')
    mood = request.form.get('mood')
    
    print(cap)
    if dim is not None:
        prompts = dim
    if ann is not None:
        prompts = prompts+" "+ann + " Avatar " 
    print(prompts)
    prompts = prompts+" with "   
    if cap is not None:
        prompts = prompts + cap
        pay+=10
    print(prompts)
    if jwellery is not None:
        prompts = prompts+", "+jwellery
        pay+=20
    print(prompts)
    if goggles is not None:
        prompts = prompts+", "+goggles
        pay+=5
    if dress is not None:
        prompts = prompts+", wearing "+dress
        pay+=15
    if mood is not None:
        prompts = prompts+", "+mood+" mood"
    print(prompts)
    img_data = avatar(prompts)
    # img_data = img_data.choices[0].text
    return json.dumps({'status':'OK','image_url' : img_data['data'][0]['url']})

    # Display or save the image
    # img.show()


@app.route('/mint',methods=['POST'])
def mint_now():
    img_url = request.form['img']
    # function to do further process of minting
    return img_url


@app.route("/payment", methods=['GET', 'POST'])
def index():
      data = pay
      return redirect(f"/{data}")

@app.route("/<upi>")
def next(upi):
  return render_template("index.html", upi=upi)


if __name__ == "__main__":
    app.run()