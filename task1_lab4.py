# TODO решите задачу
import json
def task() -> float:
    """
    Функция для вычисления суммы произведений значений "score" и "weight" из списка словарей.
    """
    with open("input.json", mode='r', encoding='utf-8') as json_file:
    # Данные JSON напрямую в коде
        data = json.load(json_file)

    # Вычисляем сумму произведений
    total_sum = sum(item.get("score", 0) * item.get("weight", 0) for item in data)

    # Округляем результат до 3 знаков
    return round(total_sum, 3)


if __name__ == "__main__":
    result = task()
    print(result)
