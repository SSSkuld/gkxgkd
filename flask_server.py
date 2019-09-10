import flask
from flask import *
app = flask.Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if flask.request.method == 'POST':
        f = flask.request.files['file']
        # f.save("./test.jpg")
        # return "upload successful"
        return render_template('result.html', t1=1, t2=1, t3=1, t4=1, t5=1, t6=1, t7=1, t8=1)


if __name__=='__main__':
    app.run()
