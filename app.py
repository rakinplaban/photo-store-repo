from flask import Flask, send_file, request
import time
import os

app = Flask(__name__)

@app.route('/anime-image')
def serve_image():
    timestamp = request.args.get('t', str(int(time.time())))  # Default to current timestamp
    image_path = "destination/anime.jpg"  # Ensure this is updated by GitHub Actions
    if not os.path.exists(image_path):
        return "Image not found", 404
    return send_file(image_path, mimetype="image/jpeg")

if __name__ == '__main__':
    app.run(debug=True)
