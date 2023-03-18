#!/usr/bin/env python3


class Temperature:
    def __init__(self, temperature: float = 0) -> None:
        self._temperature: float = temperature

    @property
    def fahrenheit_temperature(self) -> float:
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value


if __name__ == "__main__":
    room_temp: Temperature = Temperature(21)
    print(
        f"Actual room temperature is {room_temp.temperature:.2f} degrees Celsius or {room_temp.fahrenheit_temperature:.2f} Fahrenheit"
    )
