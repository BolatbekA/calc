# pip install fastapi
# pip install uvicorn
import collections
from typing import Optional

from fastapi import FastAPI, Response, status as response_status

from calculate import calculate
from history_record import HistoryRecord
from parse_string_with_exception import parse_string_with_exception
from parsing_exception import ParsingException

app = FastAPI()
app.request_history = collections.deque(maxlen=30)


@app.post('/calc/',
         description='''
Обобщённый вид арифметического выражения: [операция1](число)[(операция2)(число)]*, где:
• операция1: плюс или минус: + -
• операция2: плюс, минус, умножение, деление: + - * /
• число: положительное вещественное число (decimal), имеющее ноль и более знаков после запятой
• круглые скобки: обязательный элемент
• квадратные скобки: необязательный элемент
• звёздочка (*): ноль и более повторений
• пробелы игнорируются
''')
def calc(request: str, response: Response):
    try:
        prepared_string = request.replace(" ", "")
        parsed = parse_string_with_exception(prepared_string)

        result = calculate(parsed)

        history_record = HistoryRecord(request, str(result), 'success')
        app.request_history.append(history_record)

        return result
    except ParsingException as error:
        history_record = HistoryRecord(request)
        app.request_history.append(history_record)

        response.status_code = response_status.HTTP_400_BAD_REQUEST

        return {'error:': str(error)}


@app.get('/history',
         description='''
Возвращает последние 30 (по умолчанию) запросов к сервису в формате json (массив), где каждый запрос/ответ имеет вид:
• Успешно рассчитанный: {"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}
• Запрос с ошибкой: {"request": "5 + - 4", "response": "", "status": "fail"}
Пример ответа для двух запросов: [{"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}, {"request": "5 + - 4", "response": "", "status": "fail"}]
Дополнительные параметры запроса (могут использоваться совместно):
• limit (int) - ограничить количество выводимых запросов; при значениях меньше 1 и больше 30, возвращается ошибка;
• status (str) - отфильтровать успешные запросы или запросы с ошибкой; допустимые значения: success, fail. При других значениях возвращается ошибка.
''')
def history(response: Response, status: Optional[str] = None, limit: Optional[int] = 30):
    if limit < 1 or limit > 30:
        response.status_code = response_status.HTTP_400_BAD_REQUEST
        return {'response:': 'Limit should be between 1 and 30'}

    if status and (status != 'success' or status != 'fail'):
        response.status_code = response_status.HTTP_400_BAD_REQUEST
        return {'response:': 'Status must be either success or fail. You can skip this parameter.'}

    history = app.request_history

    status_applied = list(filter(lambda record: record['status'] == status, history) if status else history)
    limit_applied = status_applied[-1 * limit:]

    return limit_applied
