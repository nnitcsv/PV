from flask import Flask
from flask import render_template
from demos.demo import demo
from settings import DebugMode
from settings import TestingMode


app = Flask(__name__, static_folder='C:/Users/Administrator/Documents/work/nnit/E2BSubmit/E2BSubmitVue/dist/static', template_folder='C:/Users/Administrator/Documents/work/nnit/E2BSubmit/E2BSubmitVue/dist')
app.config.from_object(DebugMode)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test/')
@app.route('/test/<name>/<sex>')
def show_template(name='we', sex=None):
    return render_template('test.html', name=name, sex=sex)


app.register_blueprint(demo, url_prefix='/demos')
if __name__ == '__main__':
    app.run()
