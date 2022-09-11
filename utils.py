# Загружаем модуль json
import json


def load_candidates() -> list[dict]:
    """ Эта функция загружает данные из файла """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_candidate_by_id(candidate_id: int) -> dict:
    """Эта функция покажет кандидатов по <id>"""
    for candidate in load_candidates():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """Эта функция вернет кандидатов по <name>"""
    candidates_list_by_name = []
    for candidate in load_candidates():
        if candidate['name'] == candidate_name:
            candidates_list_by_name.append(candidate)
    return candidates_list_by_name


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    """Эта функция вернет кандидатов по навыку"""
    candidates_list_by_skill = []
    for candidate in load_candidates():
        if skill_name in candidate['skills'].lower().split(', '):
            candidates_list_by_skill.append(candidate)
    return candidates_list_by_skill



