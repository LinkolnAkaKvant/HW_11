# Загружаем Flask и необходимые функции
from flask import Flask, render_template
from utils import load_candidates, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill

# Создаем образ Flask
app = Flask(__name__)


@app.route("/")
def page_main():
    """ Эта функция открывает страницу на которой отображены все кандидаты"""
    candidates: list[dict] = load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:idx>")
def page_candidate(idx):
    """ Эта функция открывает страницу кандидата по <id> """
    candidate: dict = get_candidate_by_id(idx)
    if not candidate:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search_name(candidate_name):
    """" Эта функция открывает страницу кандидата по <name>> """
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route("/skill/<skill_name>")
def page_candidate_skill(skill_name):
    """" Эта функция открывает страниц кандидата по <skills> """
    candidates: list[dict] = get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)


@app.route('/index.html')
def my_page():
    """ Эта функция открывает страницу некого человека """
    return render_template('index.html')


# Инициализируем файл main
if __name__ == '__main__':
    app.run()
