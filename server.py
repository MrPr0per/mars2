from flask import Flask, render_template, url_for, request, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.register_form import RegisterForm
from forms.login_form import LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
info = {}


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index_main():
    return render_template('index.html', title='mars')


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


@app.route('/list_prof/<type_list>')
def list_prof_site(type_list):
    list_prof = ['инженер-исследователь',
                 'пилот',
                 'строитель',
                 'экзобиолог',
                 'врач',
                 'инженер по терраформированию',
                 'климатолог',
                 'специалист по радиационной защите',
                 'астрогеолог',
                 'гляциолог',
                 'инженер жизнеобеспечения',
                 'метеоролог',
                 'оператор марсохода',
                 'киберинженер',
                 'штурман',
                 'пилот дронов']
    return render_template('list_prof.html', type_list=type_list, list_prof=list_prof)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>анкета в космонавты</h1>
                            <div>
                                <form class="login_form" method="post">   
                                    <input class="form-control" id="shurename" aria-describedby="emailHelp" placeholder="Введите фамилию" name="shurename">
                                    <input class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>высшее</option>
                                          <option>среднее</option>
                                          <option>низшее</option>
                                          <option>окончил школу</option>
                                          <option>окончил садик</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">какова ваша профессия?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="1" value="Милиционер" checked>
                                          <label class="form-check-label" for="male">
                                            Милиционер
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="2" value="Врач">
                                          <label class="form-check-label" for="female">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="3" value="ПО-О-О-ВАР">
                                          <label class="form-check-label" for="female">
                                            Не-ет, моя главная профессия — ПО-О-О-ВАР! 
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="4" value="пилот">
                                          <label class="form-check-label" for="female">
                                            пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="5" value="строитель">
                                          <label class="form-check-label" for="female">
                                            строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="6" value="экзобиолог">
                                          <label class="form-check-label" for="female">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="7" value="врач">
                                          <label class="form-check-label" for="female">
                                            врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="8" value="инженер по терраформированию">
                                          <label class="form-check-label" for="female">
                                            инженер по терраформированию
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">почему вы хотите стать космонавтом?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form)
        global info
        info = {
            'Фамилия': str(request.form.get('shurename')),
            'Имя': str(request.form.get('name')),
            'Почта': str(request.form.get('email')),
            'Образование': str(request.form.get('class')),
            'Работа': str(request.form.get('job')),
            'Пол': str(request.form.get('sex')),
            'Мотивация': str(request.form.get('about')),
            'фото': str(request.form.get('file')),
            'готов ли остаться на марсе': str(request.form.get('accept')),
        }
        return redirect('/answer')


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    global info
    print(info)
    return render_template('anketa.html', info=info)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html')


@app.route('/jobs_list')
def jobs_list():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('jobs_list.html', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/jobs_list")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/test_img')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')
