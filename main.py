import ui
import menu
from cities import *


def main():

    list_cities = Cities.load_from_file('malopolska.csv')

    while True:
        ui.clear()
        ui.print_head("My eighborhood", "header")
        option = int(menu.main_menu())

        if option == 1:
            menu.list_statistics(list_cities)

        if option == 2:
            menu.longest_name_cities(list_cities)

        if option == 3:
            menu.largest_number_communities(list_cities)

        if option == 4:
            menu.location_more_to_one_category(list_cities)

        if option == 5:
            menu.advanced_search(list_cities)

        if option == 6:
            menu.print_nice_tree(list_cities)

        if option == 0:
            break

if __name__ == '__main__':
    main()
