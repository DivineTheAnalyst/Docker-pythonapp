from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return '''
    <h1>Welcome to Divine's Simple Web App</h1>
    <p>This is a demo web app built with Python and Flask for Containerization with Docker.</p>
    <a href="/contact">Go to Contact Page</a>
    '''

# Route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return f'''
        <h1>Thank You, {name}!</h1>
        <p>Your message: "{message}" has been received.</p>
        <a href="/">Back to Home</a>
        '''
    return '''
    <h1>Contact Us</h1>
    <form method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        <button type="submit">Send</button>
    </form>
    <a href="/">Back to Home</a>
    '''

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
