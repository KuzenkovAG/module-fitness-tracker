from dataclasses import asdict, dataclass


@dataclass
class InfoMessage:
    """Information message."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    MESSAGE = (
        'Training type: {training_type}; '
        'Duration: {duration:.3f} h.; '
        'Distance: {distance:.3f} km; '
        'Avg. speed: {speed:.3f} km/h; '
        'Spent kcal: {calories:.3f}.'
    )

    def get_message(self) -> str:
        return self.MESSAGE.format(**asdict(self))


class Training:
    """Base Training."""
    LEN_STEP = 0.65  # length of one action in meters
    M_IN_KM = 1000  # transfer from m in km
    MIN_IN_H = 60  # minutes in hour

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Get distance in km."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Get average speed."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Get spent calories."""
        return 0.0

    def show_training_info(self) -> InfoMessage:
        """Output information message about training."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories()
        )


class Running(Training):
    """Training: Run."""
    CALORIES_MEAN_SPEED_MULTIPLIER: float = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def get_spent_calories(self) -> float:
        """Get spent calories."""
        return (
            (self.CALORIES_MEAN_SPEED_MULTIPLIER
             * self.get_mean_speed()
             + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight
            / self.M_IN_KM * self.duration * self.MIN_IN_H
        )


class SportsWalking(Training):
    """Training: Sport Walking."""
    CALORIES_WEIGHT_MULTIPLIER: float = 0.035
    CALORIES_SPEED_HEIGHT_MULTIPLIER: float = 0.029
    KMH_IN_MSEC: float = round(1000 / 3600, 3)  # для перевода из км/ч в м/с
    CM_IN_M: int = 100  # для перевода из см в метры

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Get spent calories."""
        height_in_m: float = self.height / self.CM_IN_M
        mean_speed_m_in_sec: float = (
            self.get_mean_speed() * self.KMH_IN_MSEC
        )
        return (
            (self.CALORIES_WEIGHT_MULTIPLIER * self.weight
             + mean_speed_m_in_sec ** 2 / height_in_m
             * self.CALORIES_SPEED_HEIGHT_MULTIPLIER * self.weight)
            * self.duration * self.MIN_IN_H
        )


class Swimming(Training):
    """Training: Swimming."""
    LEN_STEP: float = 1.38
    CALORIES_SPEED_HEIGHT_MULTIPLIER: float = 1.1
    SWIMMING_COEFFICIENT: int = 2

    def __init__(
            self,
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
        """Get average speed."""
        return (
            self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        )

    def get_spent_calories(self) -> float:
        """Get spent calories."""
        return (
            (self.get_mean_speed()
             + self.CALORIES_SPEED_HEIGHT_MULTIPLIER)
            * self.SWIMMING_COEFFICIENT * self.weight
            * self.duration
        )


def read_package(workout_type: str, data: list) -> Training:
    """Read data."""
    training_type: dict[str, type(Training)] = {
        'RUN': Running,
        'WLK': SportsWalking,
        'SWM': Swimming
    }
    if workout_type in training_type:
        return training_type[workout_type](*data)
    raise ValueError('Не определен Training type')


def main(training: Training) -> None:
    """Output information about training."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages: list[tuple[str, list]] = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
