from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for user data (for demonstration purposes)
user_data = {}

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        number = request.form.get('number')
        email = request.form.get('email')

        # Store the data in the dictionary
        user_data['name'] = name
        user_data['number'] = number
        user_data['email'] = email

        # Redirect to the profile page
        return redirect(url_for('profile'))

    return render_template('signup.html')

# Profile page
@app.route('/profile')
def profile():
    # Pass the user data to the profile template
    return render_template('profile.html', name=user_data.get('name'), number=user_data.get('number'), email=user_data.get('email'))

if __name__ == '__main__':
    app.run(debug=True)