"""
Polymorphism in Python
From simple to interview/coding-round level.
Useful for Data Analyst and other roles.
"""


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# 1) VERY BASIC: SAME METHOD NAME, DIFFERENT OBJECTS (DUCK TYPING)
class Dog:
    def speak(self):
        return "Dog says: Woof"
class Cat:
    def speak(self):
        return "Cat says: Meow"
class Human:
    def speak(self):
        return "Human says: Hello"
def make_it_speak(living_thing):
    # Any object with speak() works here.
    return living_thing.speak()


# 2) CLASSICAL POLYMORPHISM: METHOD OVERRIDING
class Employee:
    def salary(self):
        return 0


class FullTimeEmployee(Employee):
    def salary(self):
        return 60000


class Intern(Employee):
    def salary(self):
        return 15000


# 3) BUILT-IN POLYMORPHISM
# len() works with different data types (string, list, dict, etc.)
def builtin_poly_demo():
    text = "data"
    nums = [10, 20, 30]
    info = {"name": "Asha", "role": "Analyst"}
    return len(text), len(nums), len(info)


# 4) OPERATOR OVERLOADING (ADVANCED POLYMORPHISM)
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


# 5) INTERVIEW STYLE: "COMMON INTERFACE" FOR DATA SOURCES
# Data Analyst use case: same processing code for CSV/API/Database input.
class CSVSource:
    def fetch(self):
        return [12, 18, 30, 25]


class APISource:
    def fetch(self):
        return [10, 22, 28, 40]


class DatabaseSource:
    def fetch(self):
        return [15, 19, 26, 31]


def average(values):
    return sum(values) / len(values) if values else 0


def process_source(source):
    # Polymorphism: source can be CSVSource/APISource/DatabaseSource
    records = source.fetch()
    return {
        "count": len(records),
        "min": min(records),
        "max": max(records),
        "avg": round(average(records), 2),
    }


# 6) INTERVIEW STYLE: STRATEGY POLYMORPHISM (METRIC CALCULATION)
class SumMetric:
    def calculate(self, data):
        return sum(data)


class MaxMetric:
    def calculate(self, data):
        return max(data)


class AverageMetric:
    def calculate(self, data):
        return round(average(data), 2)


def run_metric(metric, data):
    # Any class with calculate(data) can be passed.
    return metric.calculate(data)


# 7) ADVANCED: ABSTRACT-LIKE BASE CLASS (PURE PYTHON)
class Report:
    def generate(self, data):
        raise NotImplementedError("Child class must implement generate()")


class SummaryReport(Report):
    def generate(self, data):
        return f"Summary: rows={len(data)}, avg={round(average(data), 2)}"


class DetailedReport(Report):
    def generate(self, data):
        return {
            "rows": len(data),
            "sorted_data": sorted(data),
            "top_2": sorted(data, reverse=True)[:2],
        }


def build_report(report_obj, data):
    return report_obj.generate(data)


# 8) HIGH LEVEL: PLUGGABLE DATA CLEANING PIPELINE
class RemoveNegatives:
    def transform(self, data):
        return [x for x in data if x >= 0]


class CapValues:
    def __init__(self, max_value):
        self.max_value = max_value

    def transform(self, data):
        return [min(x, self.max_value) for x in data]


class RoundValues:
    def transform(self, data):
        return [round(x) for x in data]


def run_pipeline(data, steps):
    result = data
    for step in steps:
        # Polymorphism: each step object has transform()
        result = step.transform(result)
    return result


def demo():
    section("1) Basic Duck Typing")
    print(make_it_speak(Dog()))
    print(make_it_speak(Cat()))
    print(make_it_speak(Human()))

    section("2) Method Overriding")
    employees = [FullTimeEmployee(), Intern()]
    for emp in employees:
        print(emp.__class__.__name__, "salary =", emp.salary())

    section("3) Built-in Polymorphism")
    a, b, c = builtin_poly_demo()
    print("len('data') =", a)
    print("len([10,20,30]) =", b)
    print("len({'name','role'}) =", c)

    section("4) Operator Overloading")
    v1 = Vector2D(2, 3)
    v2 = Vector2D(5, 7)
    v3 = v1 + v2
    print("v1 =", v1, "v2 =", v2, "v1+v2 =", v3)

    section("5) Data Source Polymorphism (Analyst Use Case)")
    sources = [CSVSource(), APISource(), DatabaseSource()]
    for src in sources:
        print(src.__class__.__name__, "->", process_source(src))

    section("6) Strategy Polymorphism (Coding Round Pattern)")
    dataset = [20, 10, 40, 30]
    metrics = [SumMetric(), MaxMetric(), AverageMetric()]
    for m in metrics:
        print(m.__class__.__name__, "=", run_metric(m, dataset))

    section("7) Report Polymorphism")
    data = [15, 25, 35, 45]
    print(build_report(SummaryReport(), data))
    print(build_report(DetailedReport(), data))

    section("8) High-Level Pipeline Polymorphism")
    raw_data = [12.7, -3.2, 102.9, 39.1, -9.5, 80.6]
    steps = [RemoveNegatives(), CapValues(90), RoundValues()]
    cleaned = run_pipeline(raw_data, steps)
    print("Raw data    :", raw_data)
    print("Cleaned data:", cleaned)


if __name__ == "__main__":
    demo()
