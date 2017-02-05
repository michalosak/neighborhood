import ui


def main_menu():
    """main menu"""

    text_menu = """
What would you like to do:
(1) List statistics
(2) Display 3 cities with longest names
(3) Display county's name with the largest number of communities
(4) Display locations, that belong to more than one category
(5) Advanced search
(6) Print nice tree
(0) Exit program
"""
    option = ui.get_menu(text_menu, 0, 6)
    ui.clear()

    return option


def list_statistics(list_cities):
    """list statistics"""
    ui.print_head("Statistics for Małopolska", "header")
    ui.print_dictionary(list_cities.statistics(), ['Name', 'Amount'])
    input()


def longest_name_cities(list_cities):
    """longest name of cities"""

    ui.print_head("Three longest names of cities in Małopolska", "header")
    ui.print_text(", ".join(list_cities.get_longest_cities()))
    input()


def largest_number_communities(list_cities):
    """largest no of communities"""

    ui.print_head("Top 10 largest counties", "header")
    ui.print_table(list_cities.count_counties_with_communities(), ['Name', 'How many communities'])
    input()


def print_nice_tree(list_cities):

    ui.print_head("Tree", "header")
    ui.print_text(list_cities.get_nice_tree())
    input()


def location_more_to_one_category(list_cities):
    """location more to one category"""

    ui.print_head("Locations with more than 1 category", "header")
    ui.print_table(list_cities.cities_in_categories(), ['Name', 'Amount'])
    input()


def advanced_search(list_cities):
    """advenced search"""

    ui.print_head('Advanced search', 'header')
    search = ui.get_inputs(["Name: "])
    list_of_cities = list_cities.search_by_name(search[0])
    ui.clear()
    ui.print_head('Found {} entries of {}'.format(len(list_of_cities), search[0]), 'header')
    ui.print_table(list_of_cities, ['Location', 'Type'])
    input()
