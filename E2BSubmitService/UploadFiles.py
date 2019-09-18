from flask import Flask, render_template, request, abort, redirect, url_for, flash, make_response, send_from_directory
from werkzeug.utils import secure_filename
import time
import os
# import base64

app = Flask(__name__)
UPLOAD_FOLDER = 'static\\upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
base_dir = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])

alycode = 0
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'xlsx', 'xlsm', 'JPG', 'PNG', 'gif', 'GIF'])
app.secret_key = 'random string'


@app.route('/')
def index():
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    allfileset = getAllFile(base_dir)
    dic = {'allfileset': allfileset, 'code': 0}
    return render_template('index_001.html', result=dic)


@app.route('/upload')
def upload():
    return render_template('upload.html')


# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def getAllFile(dir_name):
    dirset = []
    fileset = []
    for filename in os.listdir(dir_name):
        filepath = os.path.join(dir_name, filename)
        if os.path.isdir(filepath):
            filepath = filepath.split("\\")[-1]
            dirset.append(filepath)
        else:
            filepath = filepath.split("\\")[-1]
            fileset.append(filepath)
    return [fileset, dirset]


# 上传文件
@app.route('/uploader', methods=['GET', 'POST'], strict_slashes=False)
def upload_file():
    code = 0
    if request.method == 'POST':
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        allfileset = getAllFile(base_dir)

        try:
            f = request.files["file"]
            if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
                fname = secure_filename(f.filename)
                ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
                unix_time = int(time.time())
                new_filename = fname.rsplit('.', 1)[0] + '_' + str(unix_time) + '.' + ext  # 修改了上传的文件名
                print(new_filename)
                f.save(os.path.join(base_dir, new_filename))  # 保存文件到upload目录
                # token = base64.b64encode(new_filename.encode(encoding='utf-8'))
                # print(token)
                code = 1
                allfileset = getAllFile(base_dir)
        except Exception as err:  # python 3 要这么写
            code = 2
            print('file uploaded failed: ', err)

        dic = {'allfileset': allfileset, 'code': code}
        return render_template('index_001.html', result=dic)


@app.route('/delete/<filename>', methods=['GET', 'POST'], strict_slashes=False)
def delete_file(filename):
    file = os.path.join(base_dir, filename)
    os.remove(file)
    return redirect("/")


@app.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    file_dir = os.path.join(base_dir, app.config['UPLOAD_FOLDER'])
    if request.method == 'GET':
        if filename is None:
            return 'File Not Exist!'
        else:
            response = make_response(send_from_directory(file_dir, filename, as_attachment=True))
            return response
    else:
        return 'File Not Exist!'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['name']
        if user == 'admin':
            flash('You were successfully logged in')
            return redirect(url_for('index'))
        else:
            abort(401)
            # error = 'Invalid username or password. Please try again!'
            # return render_template('login.html', error=error)
    return render_template('login.html', error=error)


@app.route('/index')
def index_01():
    return render_template('index_01.html')


if __name__ == '__main__':
    app.run()
