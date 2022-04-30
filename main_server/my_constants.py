from flask import Flask

UPLOAD_FOLDER = "C:\\Users\\hp\\Desktop\\DataShare\\upload"
DOWNLOAD_FOLDER = "C:\\Users\\hp\\Desktop\\DataShare\\download"

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp4','wav','mp3','html','doc','docx'])
app.config['BUFFER_SIZE'] = 64 * 1024
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024
