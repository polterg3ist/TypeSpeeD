from inspect import getmembers, isfunction
import os
import importlib
import importlib.util


def main():
    while True:
        parsers_list = os.listdir("parsers/")
        # remove elements that are not python file
        parsers_list = [file for file in parsers_list if len(file) > 2 and file[-3:] == '.py']

        if not parsers_list:
            return "Parsers directory is empty"

        print("Available parsers: ")
        for ind, parser in enumerate(parsers_list):
            print(f"{ind + 1}. {parser}")

        lang_ind = input("\nChoose any available parser: ")

        if lang_ind.isdigit() and len(parsers_list) + 1 > int(lang_ind) > 0:
            lang_ind = int(lang_ind) - 1
            selected_parser = parsers_list[lang_ind][:-3]  # without .py ending

            if check_module(selected_parser):
                importlib.invalidate_caches()
                imported_parser = importlib.import_module(f"parsers.{selected_parser}")
                have_parse_func = False
                module_funcs = getmembers(imported_parser, isfunction)

                for func in module_funcs:
                    if func[0] == 'parse':
                        have_parse_func = True

                if have_parse_func:
                    word_list = imported_parser.parse()
                    print("[PARSING COMPLETE]")
                    title = input("Choose a name for a title of file: ")
                    saver(word_list, title)
                    return "[PROGRAM FINISHED]"
                else:
                    print("[ERROR] Selected module doesn't have 'parse' function\n")
        else:
            print('\n[INCORRECT USER INPUT]\n')


def saver(lst, title):
    """
    List of word saver. Can handle possible duplicate names error
    """
    def write(ttl):
        with open(f"languages/{ttl}.txt", 'w') as file:
            for word in lst:
                file.write(f"{word}\n")
        print("[SAVE COMPLETED]")
        print(f"Amount of saved words - {len(lst)}")

    if os.path.exists(f"languages/{title}.txt"):
        while True:
            print("File with such name is already exist:\n1. Replace this file\n2. Change the title\n3. Exit")
            selected = input("Select any: ")
            if selected == '1':
                return write(title)
            elif selected == '2':
                while True:
                    new_title = input('Please write a new title: ')
                    if new_title != title:
                        return write(new_title)
                    else:
                        print('New title should have differences from old')
            elif selected == '3':
                break
            else:
                print(f"[ERROR] {selected} is not a supported choice")
    else:
        write(title)


def check_module(module_name):
    """
     Checks is it possible to import this module
     """
    module_spec = importlib.util.find_spec(f"parsers.{module_name}")
    if module_spec is None:
        print(f'Module: {module_name} not found')
        return None
    else:
        print(f'Module: {module_name} can be imported!')
        return module_spec


if __name__ == "__main__":
    main()
