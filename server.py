from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        text = 'Инженерные тренажеры'
        url = url_for('static', filename='img/1.png')
        alt = 'местоположение инженерных тренажеров'
    elif 'ученый' in prof:
        text = 'Научные тренажеры'
        url = url_for('static', filename='img/2.png')
        alt = 'местоположение научных тренажеров '
    else:
        text = 'такой профессии нет в списке!'
        url = url_for('static', filename='img/exit.png')
        alt = '???????????????????????????'

    return render_template('index.html', prof=prof, text=text, url=url, alt=alt)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
