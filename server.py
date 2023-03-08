from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Create a new instance of the Flask class called 'app'
@app.route('/')          # The '@' decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return the string 'Hello World!' as a response
@app.route('/play/<int:num>')
def play(num):
    return render_template('play.html', num=num)
@app.route('/play/<int:num>/<chosen_color>')
def color(num, chosen_color):
    return render_template('color.html', num=num, chosen_color=chosen_color)
if __name__=='__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.