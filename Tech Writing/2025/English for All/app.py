from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/generate')
def generate_image():
    # Same image generation code as before, but returns image directly
    img = generate_slang_image()
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

def generate_slang_image():
    # (Insert the full Python image generation code from previous answer here)
    # Return the PIL Image object
    return img  # Make sure your function returns the PIL Image

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)