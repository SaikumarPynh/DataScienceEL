import os
from flask import Flask, render_template, request, send_file
from wordcloud import WordCloud
import matplotlib.pyplot as plt

app = Flask(__name__)

# Configure a secret key for session management
app.secret_key = 'your_secret_key'

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the user input text from the form
        text = request.form['text']

        # Generate a word cloud
        wordcloud = WordCloud(width=800, height=400).generate(text)

        # Save the word cloud image
        wordcloud.to_file('static/wordcloud.png')

        # Provide a link to download the word cloud image
        return render_template('home.html', wordcloud_generated=True)

    return render_template('home.html', wordcloud_generated=False)

# Define a route to download the word cloud image
@app.route('/download')
def download():
    return send_file('static/wordcloud.png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
