class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65  # длинна одного действия в метрах
    M_IN_KM = 1000  # константа перевода м в км
    MIN_IN_H = 60  # количество минут в часе

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return 0.0

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER: float = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        result: float = ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                          * self.get_mean_speed()
                          + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight
                         / self.M_IN_KM * self.duration * self.MIN_IN_H)
        return result


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_WEIGHT_MULTIPLIER: float = 0.035
    CALORIES_SPEED_HEIGHT_MULTIPLIER: float = 0.029
    KMH_IN_MSEC: float = round(1000 / 3600, 3)  # для перевода из км/ч в м/с
    CM_IN_M: int = 100  # для перевода из см в метры

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        height_in_m: float = self.height / self.CM_IN_M
        mean_speed_m_in_sec: float = (self.get_mean_speed()
                                      * self.KMH_IN_MSEC)

        result: float = ((self.CALORIES_WEIGHT_MULTIPLIER * self.weight
                         + mean_speed_m_in_sec ** 2 / height_in_m
                         * self.CALORIES_SPEED_HEIGHT_MULTIPLIER * self.weight)
                         * self.duration * self.MIN_IN_H)

        return result


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    CALORIES_SPEED_HEIGHT_MULTIPLIER: float = 1.1
    SWIMMING_COEFFICIENT: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.count_pool = count_pool
        self.length_pool = length_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool * self.count_pool / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        result: float = ((self.get_mean_speed()
                          + self.CALORIES_SPEED_HEIGHT_MULTIPLIER)
                         * self.SWIMMING_COEFFICIENT * self.weight
                         * self.duration)
        return result


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'RUN':
        return Running(data[0], data[1], data[2])
    if workout_type == 'WLK':
        return SportsWalking(data[0], data[1], data[2], data[3])
    if workout_type == 'SWM':
        return Swimming(data[0], data[1], data[2], data[3], data[4])
    print('Не определен тип тренировки')
    return Training(0, 0.0001, 0.0001)


def main(training: Training) -> None:
    """Выводит сообщение о тренировке."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages: list[tuple[str, list]] = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
        ('WL', [9000, 1, 75, 180])
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
