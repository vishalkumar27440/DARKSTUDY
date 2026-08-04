from flask import Flask, request, send_from_directory, abort, jsonify
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
TEXT_DIR = os.path.join(BASE_DIR, "texts")
os.makedirs(TEXT_DIR, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    # If no file requested, return list of files
    fname = request.args.get("file")
    if not fname:
        files = sorted(os.listdir(TEXT_DIR))
        return jsonify({"available_files": files})

    # sanitize filename and serve
    fname = os.path.basename(fname)
    file_path = os.path.join(TEXT_DIR, fname)
    if not os.path.isfile(file_path):
        return abort(404)
    return send_from_directory(TEXT_DIR, fname, mimetype="text/plain")

@app.route("/files/<path:fname>", methods=["GET"])
def get_file(fname):
    safe = os.path.basename(fname)
    file_path = os.path.join(TEXT_DIR, safe)
    if not os.path.isfile(file_path):
        return abort(404)
    return send_from_directory(TEXT_DIR, safe, mimetype="text/plain")

# Vercel uses the WSGI app variable; expose app
# If running locally for testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
