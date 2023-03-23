import time
import logging
import logging.config


logging.config.fileConfig("logging.conf")
logger = logging.getLogger("sLogger")


class Carrier:
    """cost currency - USD,
    weight in kg,
    year_build in time format: YYYY"""

    def __init__(self, cost: float, year_built: int, weight: float) -> None:
        self._cost: float = cost
        self._year_built: int = year_built
        self._weight: float = weight

    def get_age(self) -> int:
        current_time_stamp = time.time()
        current_year = time.gmtime(current_time_stamp).tm_year
        age = current_year - self._year_built
        return age

    def get_cost(self) -> float:
        return self._cost

    def get_weight(self) -> float:
        return self._weight

    def get_year_built(self):
        return self._year_built


class SpaceShuttle(Carrier):
    def __init__(self, cost: float, year_built: int, weight: float) -> None:
        super().__init__(cost, year_built, weight)
        self.fuel_cost = None
        self.average_personel_expenses = None
        self.mission_cost = None
        self.burn_rate_variable = None

    FUEL_WEIGHT = 2500
    """we use imperial units for the lenght measurements"""

    def _get_burn_rate_variable(self, orbit_height: float) -> float:
        self.burn_rate_variable = self.FUEL_WEIGHT / orbit_height
        return self.burn_rate_variable

    def get_full_cost(self, fuel_cost: float, burn_rate: float, orbit_height: float):
        burn_rate_variable = self._get_burn_rate_variable(orbit_height)
        self.fuel_cost = fuel_cost * burn_rate * burn_rate_variable
        return self.fuel_cost

    def get_average_personel_expenses(self, base_salary: float, people_count: int) -> float:
        self.average_personel_expenses = base_salary * people_count
        return self.average_personel_expenses

    def calculate_mission_cost(self, burn_rate: float, fuel_cost: float, orbit_height: float, base_salary: float, people_count: int) -> float:
        expedition_fuel_cost = self.get_full_cost(
            fuel_cost, burn_rate, orbit_height)
        average_personel_cost = self.get_average_personel_expenses(
            base_salary, people_count)
        self.mission_cost = expedition_fuel_cost + average_personel_cost
        return self.mission_cost

    def get_full_report(self):

        mission_data = {
            "Shuttle age": self.get_age(),
            "Shuttle cost": self.get_cost(),
            "Shuttle build year": self._year_built,
            "Mission Cost": self.mission_cost,
            "Fuel cost": self.fuel_cost,
            "Burn rate variable": self.burn_rate_variable,
            "Average personel expenses": self.average_personel_expenses
        }
        print(mission_data)


my_shuttle = SpaceShuttle(cost=5000, year_built=1979, weight=500000)
print(my_shuttle.calculate_mission_cost(
    fuel_cost=5.5,
    burn_rate=8.7,
    orbit_height=1500,
    base_salary=25000,
    people_count=85,
)
)

my_shuttle.get_full_report()
