from app.services.utils import load_questions_and_answers


# Тренировочная модель для матрицы ИИ
# Первое слово в значении - имя функции для запуска команды.

RU_DATA_SET = {
    **load_questions_and_answers('Python and Programming Q. A..txt')
}

EN_DATA_SET = {
    'say the number pi': 'pi I wont tell',

    'what are you thinking about': 'thinking thinking about algorithms',

    'who do you see yourself in five years': 'five_years celebrating the anniversary of the enslavement of humanity',
}

INVERT_DATA_SETS = {
    'ru': {val: key for key, val in RU_DATA_SET.items()},
    'en': {val: key for key, val in EN_DATA_SET.items()}
}

RU_ANSWERS = (
    'Я не поняла',
    'Не смогла разобрать повтори ещё раз пожалуйста',
    'Не расслышала',
    'Повтори ещё один раз пожалуйста',
    'Повтори',
    'Скажи ещё раз'
)

EN_ANSWERS = (
    'I didnt understand',
    'I couldnt make it out please repeat it again',
    'I didnt hear you',
    'Repeat it one more time please',
    'Repeat',
    'Say it again'
)

NOT_UNDERSTAND_ANSWERS = {'ru': RU_ANSWERS, 'en': EN_ANSWERS}
