# TODO решите задачу

def task() -> float:
    """
    Функция для вычисления суммы произведений значений "score" и "weight" из списка словарей.
    """

    # Данные JSON напрямую в коде
    data = [
        {"score": 0.5, "weight": 2},
        {"score": 1.0, "weight": 1},
        {"score": 0.296, "weight": 1}
    ]

    # Вычисляем сумму произведений
    total_sum = sum(item.get("score", 0) * item.get("weight", 0) for item in data)

    # Округляем результат до 3 знаков
    return round(total_sum, 3)


if __name__ == "__main__":
    result = task()
    print(result)
