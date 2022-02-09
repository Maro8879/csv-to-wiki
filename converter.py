from csv import reader
from os import system
from os.path import isfile
from time import sleep
from math import floor
from os import name

system('color')

graphic = '''\033[1;92m
            ░█████╗░░██████╗██╗░░░██╗  ████████╗░█████╗░  ░██╗░░░░░░░██╗██╗██╗░░██╗██╗
            ██╔══██╗██╔════╝██║░░░██║  ╚══██╔══╝██╔══██╗  ░██║░░██╗░░██║██║██║░██╔╝██║
            ██║░░╚═╝╚█████╗░╚██╗░██╔╝  ░░░██║░░░██║░░██║  ░╚██╗████╗██╔╝██║█████═╝░██║
            ██║░░██╗░╚═══██╗░╚████╔╝░  ░░░██║░░░██║░░██║  ░░████╔═████║░██║██╔═██╗░██║
            ╚█████╔╝██████╔╝░░╚██╔╝░░  ░░░██║░░░╚█████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚██╗██║
            ░╚════╝░╚═════╝░░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝

            ░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
            ██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
            ██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
            ██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
            ╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
            ░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝©MadeByMaro
\033[0;0m'''


def convert(path, txt_file, caption_text='', print_bar=True):
    wiki_str = '{| class="wikitable"\n'
    wiki_str += '|+ ' + caption_text + '\n' if caption_text != '' else ''
    file = open(path, encoding='UTF-8')
    file_reader = reader(file)
    data = [row for row in file_reader]
    cols = '|-\n' + '! ' + ' !! '.join(data[0])
    wiki_str += cols
    # loading bar and converting rows process
    elem_counter = 0
    system('cls' if name == 'nt' else 'clear')
    print(graphic) if print_bar is True else None
    print(f'\033[1;92m{0:.2f}% | [{"█" * floor(0) + "░" * int(100 - floor(0))}]\033[0;0m') if print_bar is True else None
    for row in data[1:]:
        # process
        row_list = [row_element for row_element in row]
        roow = '\n|-\n' + '| ' + ' || '.join(row_list)
        wiki_str += roow
        # progress bar
        if print_bar is True:
            elem_counter += 1
            percent = elem_counter / len(data[1:]) * 100
            system('cls' if name == 'nt' else 'clear')
            print(graphic)
            print(f'\033[1;92m{percent:.2f}% | [{"█" * floor(percent) + "░" * int(100 - floor(percent))}]\033[0;0m')
    wiki_str += '\n|}'
    with open(txt_file, 'w', encoding='UTF-8') as txt:
        txt.write(wiki_str)
    file.close()


print(graphic)

# program
while True:
    list_of_errors = []
    path_to_data = input('            \033[1;92menter the path to csv file with the data | \033[0;0m')
    system('cls' if name == 'nt' else 'clear')
    print(graphic)
    caption = input('            \033[1;92menter wiki table caption (click enter to skip) | \033[0;0m')
    system('cls' if name == 'nt' else 'clear')
    print(graphic)
    path_txt = input('            \033[1;92menter the path to the txt file where you want the wiki table to be located | \033[0;0m')
    system('cls' if name == 'nt' else 'clear')
    print(graphic)
    bar, bar_value = input('            \033[1;92mdo you want to print a progress bar in terminal ?\n            It will slow down the process but you will be able to see the current progress. (Y/N) | \033[0;0m'), True
    if bar == 'Y' or bar == 'y':
        bar_value = True
    elif bar == 'N' or bar == 'n':
        bar_value = False
    else:
        list_of_errors.append('the answer to the question is incorrect')
    '' if path_to_data != '' and isfile(path_to_data) and path_to_data.endswith('.csv') else list_of_errors.append('path to the csv file is incorrect')
    '' if path_txt != '' and isfile(path_txt) and path_txt.endswith('.txt') else list_of_errors.append('path to the txt file is incorrect')
    if len(list_of_errors) == 0:
        convert(path_to_data, path_txt, caption, bar_value)
    else:
        system('cls' if name == 'nt' else 'clear')
        print(graphic, f'           \033[1;91merrors: {str(list_of_errors)}\033[0;0m\n')
    if len(list_of_errors) == 0:
        break

# end
for a in reversed(range(1, 4)):
    system('cls' if name == 'nt' else 'clear')
    print(graphic, f'            \033[1;92myour data has been converted, program will close in {a}\033[0;0m')
    sleep(1)

