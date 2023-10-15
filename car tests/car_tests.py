import pytest
from car import Car


@pytest.fixture
def car():
    return Car("Toyota", "Camry", 100)


def test_start_engine(car):
    assert car.start_engine() == "Engine started."


def test_start_engine_already_running(car):
    car.start_engine()
    assert car.start_engine() == "Engine is already running."


def test_stop_engine(car):
    car.start_engine()
    assert car.stop_engine() == "Engine stopped."


def test_stop_engine_already_off(car):
    assert car.stop_engine() == "Engine is already off."


def test_drive_with_engine_off(car):
    assert car.drive(50) == "Cannot drive. Engine is off."


def test_drive_within_miles_limit(car):
    car.start_engine()
    assert car.drive(50) == "Driving 50 miles."


def test_drive_exceed_miles_limit(car):
    car.start_engine()
    assert car.drive(150) == "The miles limit has been exceeded"


def test_drive_with_engine_off_and_zero_miles_limit():
    car = Car("Ford", "Mustang")
    assert car.drive(50) == "Cannot drive. Engine is off."


def test_drive_with_engine_already_running(car):
    car.start_engine()
    assert car.drive(50) == "Driving 50 miles."


def test_start_and_stop_engine(car):
    assert car.start_engine() == "Engine started."
    assert car.stop_engine() == "Engine stopped."
