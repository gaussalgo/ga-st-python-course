#!/usr/bin/env python3


class Temperature:
    def __init__(self, temperature: float = 0) -> None:
        self.set_temperature(temperature)

    def get_fahrenheit_temperature(self) -> float:
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self) -> float:
        return self._temperature

    # setter method
    def set_temperature(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.*")
        self._temperature: float = value


if __name__ == "__main__":
    room_temp: Temperature = Temperature(21)
    print(
        f"The room temperature is {room_temp.get_temperature():.2f} degrees Celsius or {room_temp.get_fahrenheit_temperature():.2f} Fahrenheit"
    )

    room_temp.set_temperature(19.5)
    print(
        f"The room temperature is {room_temp.get_temperature():.2f} degrees Celsius or {room_temp.get_fahrenheit_temperature():.2f} Fahrenheit"
    )
