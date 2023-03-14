book_info = (
    ("Best Mystery & Thriller","The Silent Patient",68821),
    ("Best Horror","The Institute",75717),
    ("Best History & Biography","The five",31783),
    ("Best Fiction","The Testaments",98291)
)

for category, book, votes in book_info:
    print(f"{book} won the \'{category}\' category with {votes} votes")
