from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define the root route ('/')
@app.route('/')
def home():
    """This route returns a simple welcome message."""
    return "Hello, World! Your Flask app is running. 🚀"

# Define a route that returns JSON data
@app.route('/api/data')
def get_data():
    """This route returns a sample JSON object."""
    # This data could come from a database, another API, etc.
    sample_data = {
    "approved": {
        "onedrive": "Secure file storage and sharing",
        "miro": "Collaborative design tool"
    },
    "unapproved": {
        "dropbox": "Not approved for enterprise use",
        "figma": "Not approved for enterprise use",
        "chatgpt": "Not approved for enterprise use"
    }
}
    # jsonify converts the Python dictionary to a JSON response
    return jsonify(sample_data)

# This is only for local testing, Vercel will use its own server
if __name__ == '__main__':
    app.run(debug=True)