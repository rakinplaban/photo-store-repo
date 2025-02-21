from flask import Flask, send_file, request, make_response
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
import sys

app = Flask(__name__)

@app.route('/anime-image')
def serve_image():
    # timestamp = request.args.get('t', str(int(time.time())))  # Default to current timestamp
    # image_path = "destination/anime.jpg"  # Ensure this is updated by GitHub Actions
    # if not os.path.exists(image_path):
    #     return "Image not found", 404
    # return send_file(image_path, mimetype="image/jpeg")

    response = make_response(send_file("destination/anime.webp", mimetype='image/jpeg'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


def update_images():
    print("Updating images... 🚀")
    try:
        # Run your existing image update script
        subprocess.run(["python", "script.py"], check=True)
        print("Images updated successfully! 🌟")
    except Exception as e:
        print(f"Error updating images: {e}")


# Set up a scheduler to run the update_images function every 5 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(update_images, "interval", minutes=2)
scheduler.start()


if __name__ == '__main__':
    print(sys.executable)
    app.run(debug=False, use_reloader=False)
