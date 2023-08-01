def find_smaller_digits(ls: list) -> list:
    result = []
    for idx in range(len(ls)):
        curr_result = 0
        for j in range(idx + 1, len(ls)):
            if (ls[idx] > ls[j]):
                curr_result += 1
        result.append(curr_result)
    return result


def get_product_id(url: str) -> str:
    start = url.find("-p-") + 3
    cutted_url = url[start:]
    end = cutted_url.find("-")
    return url[start:end]
#  >> product id is 90764

# exampleshop.com/dry-water-just-add-water-to-get-water-p-147-24122017.html >> product id is 147

# exampleshop.com/public-toilet-proximity-radar-p-942312798-01012020.html >> product id is 942312798


# print(get_product_id("exampleshop.com/fancy-coffee-cup-p-90764-12052019.html"))


def product_list(numbers: list) -> list:
    product_of_all_elements = 1
    for number in numbers:
        product_of_all_elements *= number
    return [product_of_all_elements // number for number in numbers]


print(product_list([1, 5, 2]))
