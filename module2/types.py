def parse_students(students_data: str) -> list[str]:
    return students_data.split(", ")


print('Hi')
print(parse_students("sasha, masha, dasha"))
