import flask
app = flask.Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if flask.request.method == 'POST':
        f = flask.request.files['file']
        f.save("./test.jpg")
        return "upload successful"


if __name__=='__main__':
    app.run()
