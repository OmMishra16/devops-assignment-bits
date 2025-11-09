from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
        <head><title>Docker Demo</title></head>
        <body>
            <h1>Hello from Docker Container!</h1>
            <p>This application is running inside a Docker container.</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)