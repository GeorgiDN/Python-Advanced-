def classify_books(*args, **kwargs):
    isbn_codes_books = {}

    for code, book in kwargs.items():
        isbn_codes_books[book] = code

    fiction_books = {}
    non_fiction_books = {}

    for kind, title in args:
        if kind == 'fiction':
            fiction_books[title] = isbn_codes_books[title]
        elif kind == 'non_fiction':
            non_fiction_books[title] = isbn_codes_books[title]

    result = []

    if fiction_books:
        sorted_fiction_books = dict(sorted(fiction_books.items(), key=lambda x: x[1]))
        result.append('Fiction Books:')
        for book, isbn_code in sorted_fiction_books.items():
            result.append(f'~~~{isbn_code}#{book}')

    if non_fiction_books:
        sorted_non_fiction_books = dict(sorted(non_fiction_books.items(), key=lambda x: x[1], reverse=True))
        result.append('Non-Fiction Books:')
        for book, isbn_code in sorted_non_fiction_books.items():
            result.append(f'***{isbn_code}#{book}')

    return '\n'.join(result)

# print(classify_books(
#     ("fiction", "Brave New World"),
#     ("non_fiction", "The Art of War"),
#     NF3421NN="The Art of War",
#     FF1234UU="Brave New World"
# ))


# print(classify_books(
#     ("non_fiction", "The Art of War"),
#     ("fiction", "The Great Gatsby"),
#     ("non_fiction", "A Brief History of Time"),
#     ("fiction", "Brave New World"),
#     FF1234HH="The Great Gatsby",
#     NF3845UU="A Brief History of Time",
#     NF3421NN="The Art of War",
#     FF1234UU="Brave New World"
# ))


# print(classify_books(
#     ("fiction", "Brave New World"),
#     ("fiction", "The Catcher in the Rye"),
#     ("fiction", "1984"),
#     FICCITRZZ="The Catcher in the Rye",
#     FIC1984XX="1984",
#     FICBNWYYY="Brave New World"
# ))
