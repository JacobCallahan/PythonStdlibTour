import json


class JSONSerialize:
    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        return cls(**json.loads(json_str))


class Person(JSONSerialize):
    def __init__(self, name, age, fear):
        self.name = name
        self.age = age
        self.fear = fear

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, fear={self.fear})"


alice = Person(name="Alice", age=30, fear="Spiders")
