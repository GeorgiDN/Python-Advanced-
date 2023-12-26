def word_filter(text):
    result = [product for product in text if len(product) % 2 == 0]
    return result


def print_result(txt):
    return [print(word) for word in txt]


products = input().split(" ")
print_result(word_filter(products))



# One row
#print('\n'.join([product for product in input().split(" ") if len(product) % 2 == 0]))
