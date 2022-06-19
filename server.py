from flask import Flask # подключаем библиотеки
from flask import request
import json

app = Flask(__name__) # Приложение

def load_json(filename): # функция для загрузки файла
    with open(filename, 'r') as file: # открываем
        data = json.load(file) # загружаем
    return data # возвращаем

def create_id(data): # создание id с помощью сложения всех данных пользователя
    return ''.join(data) # возвращаем

def to_json(dct, filename): # загрузка в файл
    with open(filename, 'w') as file: # открываем
        json.dump(dct, file, ensure_ascii=False) # загружаем


@app.route('/chg_nme', methods=['POST', 'GET']) # ссылка для смены имени
def form_change_name():
    if request.method == 'GET': # если get
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Сменить имя пользователя</title>
                          </head>
                          <body>
                            <h1>Сменить имя пользователя</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" placeholder="Логин" name="email"><br>
                                    <input type="password" class="form-control" id="password" placeholder="Пароль" name="password"><br>
                                    <input type="text" class="form-control" id="name" placeholder="Новое имя" name="name"><br>
                                    <button type="submit" class="btn btn-primary">Сменить</button>
                                    <a href="/">В меню</a>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST': # если post
        email = request.form['email'] # логин (почта)
        password = request.form['password'] # пароль
        name = request.form['name'] # новое имя
        data = load_json('data.json') # загружаем файл
        flag1 = False # два флага для проверки нормальности введеных данных
        flag2 = False
        for i in range(len(data)): # для каждого проверяем паоль и логин
            if data[i]['email'] == email: # если подходит
                if data[i]['password'] == password: # и то и другое
                    flag2 = True
                else:
                    flag2 = False
                flag1 = True # если да
                data[i]['name'] = name # Изменяем имя
                break
        if not flag1: # если логин не найден
            return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Неуспешно</title>
                      </head>
                      <body>
                        <h1>Такого пользователя не существует</h1>
                        <a href="/chg_nme">Назад</a>
                      </body>
                    </html>'''

        elif not flag2: # если пароль не подходит
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Неуспешно</title>
                              </head>
                              <body>
                                <h1>Пароль неверный</h1>
                                <a href="/chg_nme">Назад</a>
                              </body>
                            </html>'''
        else: # если все ок
            to_json(data, "data.json") # загрцжаем в файл
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Успешно</title>
                              </head>
                              <body>
                                <h1>Имя изменено успешно</h1>
                                <a href="/">В меню</a>
                              </body>
                            </html>'''


@app.route('/chg_age', methods=['POST', 'GET'])
def form_change_age(): # смена возраста
    # Все то же самое, только с возрастом
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
                            <title>Сменить возраст пользователя</title>
                          </head>
                          <body>
                            <h1>Сменить возраст пользователя</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" placeholder="Логин" name="email"><br>
                                    <input type="password" class="form-control" id="password" placeholder="Пароль" name="password"><br>
                                    <input type="number" class="form-control" id="age" placeholder="Новый возраст" name="age"><br>
                                    <button type="submit" class="btn btn-primary">Сменить</button>
                                    <a href="/">В меню</a>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        age = request.form['age']
        data = load_json('data.json')
        flag1 = False
        flag2 = False
        for i in range(len(data)):
            if data[i]['email'] == email:
                if data[i]['password'] == password:
                    flag2 = True
                else:
                    flag2 = False
                flag1 = True
                data[i]['age'] = age
                break
        if not flag1:
            return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Неуспешно</title>
                      </head>
                      <body>
                        <h1>Такого пользователя не существует</h1>
                        <a href="/chg_age">Назад</a>
                      </body>
                    </html>'''

        elif not flag2:
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Неуспешно</title>
                              </head>
                              <body>
                                <h1>Пароль неверный</h1>
                                <a href="/chg_age">Назад</a>
                              </body>
                            </html>'''
        else:
            to_json(data, "data.json")
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Успешно</title>
                              </head>
                              <body>
                                <h1>Возраст изменен успешно</h1>
                                <a href="/">В меню</a>
                              </body>
                            </html>'''


@app.route('/chg_pas', methods=['POST', 'GET'])
def form_change_pas():  # смена пароля
    # все то же самое только с паролем
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
                            <title>Сменить пароль пользователя</title>
                          </head>
                          <body>
                            <h1>Сменить пароль пользователя</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" placeholder="Логин" name="email"><br>
                                    <input type="password" class="form-control" id="password" placeholder="Пароль" name="password"><br>
                                    <input type="password" class="form-control" id="password2" placeholder="Новый пароль" name="password2"><br>
                                    <button type="submit" class="btn btn-primary">Сменить</button>
                                    <a href="/">В меню</a>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        data = load_json('data.json')
        flag1 = False
        flag2 = False
        for i in range(len(data)):
            if data[i]['email'] == email:
                if data[i]['password'] == password:
                    flag2 = True
                else:
                    flag2 = False
                flag1 = True
                data[i]['password'] = password2
                break
        if not flag1:
            return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Неуспешно</title>
                      </head>
                      <body>
                        <h1>Такого пользователя не существует</h1>
                        <a href="/chg_age">Назад</a>
                      </body>
                    </html>'''

        elif not flag2:
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Неуспешно</title>
                              </head>
                              <body>
                                <h1>Пароль неверный</h1>
                                <a href="/chg_age">Назад</a>
                              </body>
                            </html>'''
        else:
            to_json(data, "data.json")
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Успешно</title>
                              </head>
                              <body>
                                <h1>Пароль изменен успешно</h1>
                                <a href="/">В меню</a>
                              </body>
                            </html>'''


@app.route('/chg_srn', methods=['POST', 'GET'])
def form_change_surname(): # смена фамилии
    # все то же самое только с фамилией
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
                            <title>Сменить фамилию пользователя</title>
                          </head>
                          <body>
                            <h1>Сменить фамилию пользователя</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" placeholder="Логин" name="email"><br>
                                    <input type="password" class="form-control" id="password" placeholder="Пароль" name="password"><br>
                                    <input type="text" class="form-control" id="surname" placeholder="Новая фамилия" name="surname"><br>
                                    <button type="submit" class="btn btn-primary">Сменить</button>
                                    <a href="/">В меню</a>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        surname = request.form['surname']
        data = load_json('data.json')
        flag1 = False
        flag2 = False
        for i in range(len(data)):
            if data[i]['email'] == email:
                if data[i]['password'] == password:
                    flag2 = True
                else:
                    flag2 = False
                flag1 = True
                data[i]['surname'] = surname
                break
        if not flag1:
            return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Неуспешно</title>
                      </head>
                      <body>
                        <h1>Такого пользователя не существует</h1>
                        <a href="/chg_srn">Назад</a>
                      </body>
                    </html>'''

        elif not flag2:
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Неуспешно</title>
                              </head>
                              <body>
                                <h1>Пароль неверный</h1>
                                <a href="/chg_srn">Назад</a>
                              </body>
                            </html>'''
        else:
            to_json(data, "data.json")
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Успешно</title>
                              </head>
                              <body>
                                <h1>Фамилия изменена успешно</h1>
                                <a href="/">В меню</a>
                              </body>
                            </html>'''

@app.route('/del_user', methods=['POST', 'GET'])
def form_del(): # удаление пользователя
    if request.method == 'GET': # если get
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Удаление пользователей</title>
                          </head>
                          <body>
                            <h1>Удаление пользователей</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" placeholder="Логин" name="email"><br>
                                    <input type="password" class="form-control" id="password" placeholder="Пароль" name="password"><br>
                                    <button type="submit" class="btn btn-primary">Удалить</button>
                                    <a href="/">В меню</a>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST': # если post
        email = request.form['email'] # берем логин и пароль
        password = request.form['password']
        data = load_json('data.json') # загрцжаем данные
        flag1 = False
        flag2 = False
        for i in range(len(data)):
            if data[i]['email'] == email:
                if data[i]['password'] == password:
                    flag2 = True
                else:
                    flag2 = False
                flag1 = True
                data[i] = '' # если и пароль и логин верные то удаляем
                break
        if not flag1: # еслти логина нет
            return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Неуспешно</title>
                      </head>
                      <body>
                        <h1>Такого пользователя не существует</h1>
                        <a href="/del_user">Назад</a>
                      </body>
                    </html>'''

        elif not flag2: # если пароль неверный
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Неуспешно</title>
                              </head>
                              <body>
                                <h1>Пароль неверный</h1>
                                <a href="/del_user">Назад</a>
                              </body>
                            </html>'''
        else: # иначе
            to_json([i for i in data if i != ''], "data.json") # добавляем все кроме удаленного
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <title>Успешно</title>
                              </head>
                              <body>
                                <h1>Пользователь удален</h1>
                                <a href="/">В меню</a>
                              </body>
                            </html>'''


@app.route('/add_user', methods=['POST', 'GET'])
def form_add(): # добавление
    if request.method == 'GET': # если get
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Регистрация пользователей</title>
                          </head>
                          <body>
                            <h1>Регистрация</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Имя" name="name"><br>
                                    <input type="text" class="form-control" id="surname" placeholder="Фамилия" name="surname"><br>
                                    <input type="number" class="form-control" id="age" placeholder="Возраст" name="age"><br>
                                    <input type="email" class="form-control" id="email" placeholder="Логин" name="email"><br>
                                    <input type="password" class="form-control" id="password" placeholder="Пароль" name="password"><br>
                                    <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
                                    <a href="/">В меню</a>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST': # если post
        dct = {'name': request.form['name'], # создаем словарь из полученных данных
               'surname': request.form['surname'],
               'age': request.form['age'],
               'email': request.form['email'],
               'password': request.form['password']}
        for_id = [dct['name'], dct['surname'], dct['age'], dct['email']] # создаем id
        id = create_id(for_id)
        login = dct['email']
        dct['id'] = id # в словарь кладем id
        data = load_json('data.json') # загружаем файл
        for i in data: # сверяем каждый логин
            if i['email'] == login: # если такой логин есть
                return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Неуспешно</title>
                          </head>
                          <body>
                            <h1>Логин занят</h1>
                            <a href="/add_user">Назад</a>
                          </body>
                        </html>'''
        data.append(dct) # добавляем в файл нового пользователя
        to_json(data, "data.json")
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Успешно</title>
                          </head>
                          <body>
                            <h1>Пользователь зарегистрирован</h1>
                            <a href="/">В меню</a>
                          </body>
                        </html>'''

@app.route('/all', methods=['GET']) # вывод всех пользователей для проверки
def form_all():
    if request.method == 'GET': # если get
        data = load_json('data.json') # загружанем файл
        if data != []: # если он не пустой
            countdown_list = [f'<h3>{" ".join(data[0])}</h3>'] + [f'<h3>{" ".join(i[j] for j in i)}</h3>' for i in data if data != []] # составляем списко для вывода
        else:
            countdown_list = ['<h2>NO PERSONS</h2>'] # если пустой то в списке только одно значение
        # выводим
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Все пользователи</title>
                          </head>
                          <body>
                            <h1>Все пользователи</h1>
                            <div>
                            {'</br>'.join(countdown_list)}<br>
                            <a href="/">В меню</a><br>
                            </div>
                          </body>
                        </html>'''

@app.route('/', methods=['GET']) # основная страница
# здесь выводим ссылки на все страницы операций
def form_main():
    if request.method == 'GET': # если get
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Операции с пользователями</title>
                          </head>
                          <body>
                            <h1>Операции с пользователями</h1>
                            <div>  
                            <a href="/add_user"><h3>Регистрация<h3></a><br>
                            <a href="/del_user"><h3>Удаление<h3></a><br>
                            <a href="/chg_srn"><h3>Смена фамилии<h3></a><br>
                            <a href="/chg_nme"><h3>Смена имени<h3></a><br>
                            <a href="/chg_age"><h3>Смена возраста<h3></a><br>
                            <a href="/chg_pas"><h3>Смена пароля<h3></a><br>
                            <a href="/all"><h3>Все пользователи<h3></a><br>
                            </div>
                          </body>
                        </html>'''

if __name__ == '__main__': # запуск
    app.run(port=5050, host='127.0.0.1')