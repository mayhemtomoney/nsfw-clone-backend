from flask import Flask, request, jsonify
import replicate
import os

app = Flask(__name__)
replicate_token = os.environ.get("REPLICATE_API_TOKEN")
os.environ["REPLICATE_API_TOKEN"] = replicate_token

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    try:
        output = replicate.run(
            "andreasjansson/stable-diffusion",
            input={"prompt": prompt}
        )
        return jsonify({"image_url": output[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def home():
    return "NSFW Clone Generator is live."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
