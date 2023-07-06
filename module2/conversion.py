owner = ""

if owner:
    print('I have owner')

if owner is not None:
    print('I have owner')


def can_they_book(adults_count: int = 0, children_count: int = 0) -> bool:
    if (adults_count + children_count > 8 or adults_count < 1 or
            children_count // adults_count > 2):
        return False
    return True


def recommend_room(
    adults_count: int = 0,
    children_count: int = 0,
    babies_count: int = 0
) -> str:
    with_babies = adults_count + children_count + babies_count

    if (with_babies <= 4):
        return "small room"
    elif (with_babies == 5 and babies_count == 1):
        return "small room + extra bed"
    elif (with_babies <= 8):
        return "big room"
    elif (with_babies == 9 and babies_count == 1):
        return "big room + extra bed"


print(recommend_room(2, 2, 1))
print(recommend_room(2, 1, 1))
print(recommend_room(3, 0, 2))
