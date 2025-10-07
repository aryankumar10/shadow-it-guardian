from flask import Flask, jsonify, request

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
    user_dept_query = request.args.get('userdept')

    if user_dept_query:
        found_key = None
        for key in sample_data.keys():
            if key.lower() == user_dept_query.lower():
                found_key = key
                break
        
        if found_key:
            counts = sample_data.get(found_key)
            return jsonify({"counts": counts})
        else:
            return jsonify({"error": "Department not found"}), 404
    else:
        return jsonify(sample_data)


@app.route('/api/employees_min')
def get_data_2():
    sample_data = {
        "IT Manager": 1,
        "IT Developer": 4,
        "LOGISTIC Manager": 2,
        "LOGISTIC Employee": 8
    }
    user_dept_query = request.args.get('userdept')

    if user_dept_query:
        found_key = None
        for key in sample_data.keys():
            if key.lower() == user_dept_query.lower():
                found_key = key
                break
        
        if found_key:
            counts = sample_data.get(found_key)
            return jsonify({"counts": counts})
        else:
            return jsonify({"error": "Department not found"}), 404
    else:
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

    user_email = request.args.get('useremail')
    if user_email:
        department = sample_data.get(user_email)
        if department:
            return jsonify({"department": department})
        else:
            return jsonify({"error": "User email not found"}), 404
    else:
        return jsonify(sample_data)


@app.route('/api/depts_msgs')
def get_data_4():
    sample_data = {
        "IT Manager": "Cannot take leave due to minimum IT Manager required rule",
        "IT Developer": "Cannot take leave due to minimum IT Developer required rule",
        "LOGISTIC Manager": "Cannot take leave due to minimum LOGISTIC Manager required rule",
        "LOGISTIC Employee": "Cannot take leave due to minimum LOGISTIC Employee required rule"
    }
    user_dept_query = request.args.get('userdept')

    if user_dept_query:
        found_key = None
        for key in sample_data.keys():
            if key.lower() == user_dept_query.lower():
                found_key = key
                break
        
        if found_key:
            message = sample_data.get(found_key)
            return jsonify({"message": message})
        else:
            return jsonify({"error": "Department not found"}), 404
    else:
        return jsonify(sample_data)


# This is only for local testing, Vercel will use its own server
if __name__ == '__main__':
    app.run(debug=True)