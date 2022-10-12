from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, I am running on remote code-server</p>"


if __name__ == '__main__':
    # The flask run command can do more than just start the development server.
    # By enabling debug mode, the server will automatically reload if code changes,
    # and will show an interactive debugger in the browser if an error occurs during a request.
    app.run(host='0.0.0.0', debug=True)

