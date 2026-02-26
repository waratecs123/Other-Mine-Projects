import datetime
from .data.languages import LANGUAGES


def auto_docstr_readme(func=None, language=None, visualization=None, write_document=None):
    """A decorator that automatically creates a README for all the functions it applies to"""
    if language not in LANGUAGES.keys():
        language = 'en'

    if visualization not in [True, False]:
        visualization = False

    if write_document not in [True, False]:
        write_document = True

    auto_docstr_readme.counter = 0
    answer_lst = LANGUAGES[language]

    if write_document:
        with open("../README.md", "w", encoding="utf-8") as file:
            file.write(f"_{answer_lst[7]}_\n\n")
            file.write(f"_{answer_lst[8]}: {datetime.datetime.now()}_\n\n")

    def decorator(func):
        def wrapper(*args, **kwargs):
            auto_docstr_readme.counter += 1
            N_A = answer_lst[6]

            result = func(*args, **kwargs)

            name = func.__name__
            about = func.__doc__.strip() if func.__doc__ else N_A
            input_data = ", ".join(func.__code__.co_varnames) or N_A
            args_str = ", ".join(str(arg) for arg in args)
            kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())

            text = (f"## {answer_lst[1]}: {name}\n\n"
                    f"{answer_lst[0]}: {auto_docstr_readme.counter}\n\n"
                    f"{answer_lst[2]}: {about}\n\n"
                    f"{answer_lst[3]}: {input_data if input_data else N_A}\n\n"
                    f"{answer_lst[4]}: {args_str if args_str else N_A}\n\n"
                    f"{answer_lst[5]}: {kwargs_str if kwargs_str else N_A}\n\n"
                    f"{answer_lst[9]}: {result}\n\n"
                    f"---\n\n")

            if visualization:
                print(text)

            with open("../README.md", "a", encoding="utf-8") as file_1:
                file_1.write(text)

            return result

        return wrapper

    if func is not None:
        return decorator(func)

    return decorator
