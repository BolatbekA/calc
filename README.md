# Сервис-калькулятор
С помощью фреймворка FastAPI реальзован сервис, вычисляющий результат арифметического выражения и предоставляющий возможность просмотреть история запросов.
Сервис соответствует Rest соглашениям: Get, Post запросы, HTTP коды ответов и т.д.
Сервис "самодокументированный" - предоставляет описание форматов данных и запросов/ответов в формате OpenAPI с интерфейсом Swagger.
Описание конечных точек (endpoints)

## /calc
Принимает в качестве входного значения арифметическое выражение и выдаёт либо ответ, либо ошибку.
Обобщённый вид арифметического выражения: [операция1](число)[(операция2)(число)]*, где:
• операция1: плюс или минус: + -
• операция2: плюс, минус, умножение, деление: + - * /
• число: положительное вещественное число (decimal), имеющее ноль и более знаков после запятой
• круглые скобки: обязательный элемент
• квадратные скобки: необязательный элемент
• звёздочка (*): ноль и более повторений
• пробелы игнорируются
Примеры выражений и результат расчёта (информация по расчёту: см. ниже):
• +100.1 → 100.1
• -0 → 0
• -7 / 34.2 → -0.205
• - 6 * 2 → -12
• 2. / 1. → 2
• 5 + - 4 → ошибка
• *1 + 7 → ошибка
• 4 / 3 + → ошибка
Замечания по расчёту:
• арифметический приоритет операций игнорируется – все операции выполняются слева направо, то есть
выражение 5 - 4 * 2 считается как (5 - 4) * 2, результат: 2
• количество значащих цифр после запятой: до 3 включительно, незначащих нули должны быть обрезаны
• округление математическое: 1.1234 → 1.123, 1.1235 → 1.124

## /history
Конечная точка возвращает последние 30 (по умолчанию) запросов к сервису в формате json (массив), где каждый
запрос/ответ имеет вид:
• Успешно рассчитанный: {"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}
• Запрос с ошибкой: {"request": "5 + - 4", "response": "", "status": "fail"}
Пример ответа для двух запросов:
[{"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}, {"request": "5+ - 4", "response": "", "status": "fail"}]
Дополнительные параметры запроса (могут использоваться совместно):
• limit (int) - ограничивает количество выводимых запросов; при значениях меньше 1 и больше 30,
возвращается ошибка;
• status (str) - отфильтровывает успешные запросы или запросы с ошибкой; допустимые значения: success, fail.
При других значениях возвращается ошибка.

Все зависимости находятся в requirements.txt
После установки зависимостей необходимо выполнить команду для запуска из дериктории calculator: uvicorn api:app --reload  
