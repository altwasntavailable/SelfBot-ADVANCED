from flask import Flask, redirect, render_template
from threading import Thread
import markdown

app = Flask(__name__)

def render_markdown(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return markdown.markdown(content)

@app.route('/')
def home():
    readme_html = render_markdown('README.md')
    return '''
        <html>
        <head>
            <title>Selfbot</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #333333; /* Dark background color */
                    padding: 20px;
                    color: #ffffff; /* White text color */
                }}
        
                h1 {{
                    color: #FFFFFF; /* Deep pink heading color */
                    text-align: center;
                }}
        
                .container {{
                    max-width: 800px;
                    margin: 0 auto;
                    background-color: #646464; /* Dark orange container color */
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }}
        
                .button {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #00BFFF; /* Deep sky blue button color */
                    color: #ffffff; /* White text color */
                    text-decoration: none;
                    border-radius: 4px;
                    transition: background-color 0.3s ease;
                }}
        
                .button:hover {{
                    background-color: #1E90FF; /* Dodger blue hover color */
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Selfbot</h1>
                {readme_html}
                <a href="https://github.com/altwasntavailable/SelfBot-ADVANCED" class="button">GitHub</a>
                <a href="https://github.com/altwasntavailable/SelfBot-ADVANCED/blob/main/LICENSE" class="button">MIT LICENSE</a>
            </div>
        </body>
        </html>
    '''.format(readme_html=readme_html)

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
