from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure your database connection
db = mysql.connector.connect(
    host="localhost",
    user="literature",
    password="hub123",
    database="literature_hub"  # Updated database name
)

# Define a route to handle the HTML page
@app.route('/')
def index():
    return render_template('your_html_page.html')

# Define a route to handle the form submission
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    if request.method == 'POST':
        # Get data from the form
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        feedback_message = request.form['feedbackMessage']

        # Insert feedback data into the database
        cursor = db.cursor()
        insert_query = "INSERT INTO feedback (first_name, last_name, email, message) VALUES (%s, %s, %s, %s)"
        data = (fname, lname, email, feedback_message)
        
        try:
            cursor.execute(insert_query, data)
            db.commit()
            cursor.close()
        except mysql.connector.Error as err:
            db.rollback()
            cursor.close()
            return "Error: " + str(err)

        # Fetch all feedback messages from the database (for displaying later)
        cursor = db.cursor()
        select_query = "SELECT * FROM feedback"
        cursor.execute(select_query)
        feedback_messages = cursor.fetchall()
        cursor.close()

        return render_template('your_html_page.html', feedback_messages=feedback_messages)

if __name__ == '__main__':
    app.run(debug=True)
