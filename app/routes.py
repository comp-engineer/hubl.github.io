from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Set up the database connection
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

@app.route('/')
def index():
    # Use the database connection to execute queries
    cursor = db.cursor()
    cursor.execute("SELECT * FROM your_table")
    results = cursor.fetchall()

    # Process the data
    documents = []  # Create an empty list to store the data

    for row in results:
        # Assuming your table has columns named 'title', 'image', 'description', 'price', and 'link'
        document = {
            'title': row[0],
            'image': row[1],
            'description': row[2],
            'price': row[3],
            'link': row[4]
        }
        documents.append(document)

    # Close the cursor
    cursor.close()

    # Pass the data to your template
    return render_template('your_template.html', documents=documents)

if __name__ == '__main__':
    app.run()
