from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filestorage.db'
db = SQLAlchemy(app)

class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputfile']
    newFile = FileContents(name = file.filename, data=file.read())
    db.session.add(newFile)
    db.session.commit()
    return 'Saved '+ file.filename + ' to the database!'

@app.route('/download', methods=['POST'])
def download():
    file_data = FileContents.query.filter_by(id=9).first()
    return send_file(BytesIO(file_data.data), attachment_filename='downloaded_image.jpeg',mimetype='image/jpeg', as_attachment=True)

if __name__ == '__main__':
    app.run(host='169.254.62.55',port=5000,debug=True)


