def get_full_name(first_name: str, last_name: str):
    return first_name.title() + " " + last_name.title()


print(get_full_name("sohan", "kathait"))


def get_name_with_age(name: str, age: int):
    name_with_age: str
    name_with_age = name + " is this old " + str(age)
    return name_with_age


print(get_name_with_age("sohan", 23))


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool,
              item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


print(get_items("sohan", 23, 1.0, False, bytes([1, 2])))


def process_items(items: list[str]):
    for item in items:
        print(item.capitalize())


process_items(["sohan", "kathait", "1"])


def process_items2(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


process_items2((1, 2, "sohan"), {bytes([1, 2]), bytes([3, 4])})


def process_items3(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


process_items3({"amount": 23.3})


def process_item4(item: int | str):
    print(item)


process_item4(1)
process_item4("sohan")


def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


say_hi("sohan")
say_hi(None)
say_hi()


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name
