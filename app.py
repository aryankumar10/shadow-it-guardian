from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define the root route ('/')
@app.route('/')
def home():
    """This route returns a simple welcome message."""
    return "Hello, World! Your Flask app is running. 🚀"

# Define a route that returns JSON data
@app.route('/api/employees_current')
def get_data_1():
    sample_data = {
        "IT Manager": 2,
        "IT Developer": 6,
        "LOGISTIC Manager": 4,
        "LOGISTIC Employee": 8
    }
    return jsonify(sample_data)


@app.route('/api/employees_min')
def get_data_2():
    sample_data = {
        "IT Manager": 1,
        "IT Developer": 4,
        "LOGISTIC Manager": 2,
        "LOGISTIC Employee": 8
    }
    return jsonify(sample_data)

@app.route('/api/employees_depts')
def get_data_3():
    sample_data = {
        "everett.allen741@moveworkslabs.com": "IT Manager",
        "it_manager@moveworkslabs.com": "IT Manager",
        "it_developer@moveworkslabs.com": "IT Developer",
        "logistic_manager@moveworkslabs.com": "LOGISTIC Manager",
        "logistic_employee@moveworkslabs.com": "LOGISTIC Employee"
    }
    return jsonify(sample_data)

@app.route('/api/depts_msgs')
def get_data_4():
    sample_data = {
        "IT Manager": "Cannot take leave due to minimum IT Manager required rule",
        "IT Developer": "Cannot take leave due to minimum IT Developer required rule",
        "LOGISTIC Manager": "Cannot take leave due to minimum LOGISTIC Manager required rule",
        "LOGISTIC Employee": "Cannot take leave due to minimum LOGISTIC Employee required rule"
    }
    return jsonify(sample_data)


# This is only for local testing, Vercel will use its own server
if __name__ == '__main__':
    app.run(debug=True)