import common
import operator


class Cities:

    def __init__(self, list_of_cities):

        self.list_of_cities = list_of_cities

    def get_longest_cities(self, how_many=3):
        """get city names
        Args: how_many
        Returns: list of cities with longest names
        """

        len_of_cities_list = dict()
        for i, city in enumerate(self.list_of_cities):
            len_of_cities_list[i] = len(city.city_name)

        sorted_len = sorted(len_of_cities_list.items(), key=operator.itemgetter(1))

        return [self.get_city_by_id(id[0]) for id in sorted_len[-how_many:]]

    def get_city_by_id(self, id):
        """get city name by id
        Args: id
        Returns: name of city
        """
        return self.list_of_cities[id].city_name

    def statistics(self):
        """create table with statistics count zones in every pow
        returns: dictionary
        """
        dict_of_cities = dict()

        for city in self.list_of_cities:

            if city.type_of_city in dict_of_cities.keys():
                dict_of_cities[city.type_of_city] += 1
            else:
                dict_of_cities[city.type_of_city] = 1

        return dict_of_cities

    def cities_in_categories(self):
        """fount city in categories"""

        cities_in_cats = dict()
        for city in self.list_of_cities:
            if city.city_name in cities_in_cats.keys():
                cities_in_cats[city.city_name] += 1
            else:
                cities_in_cats[city.city_name] = 1

        cities_in_cat = dict((city, amount) for city, amount in cities_in_cats.items() if int(amount) > 1)
        # get dict if value more than 1

        cities_in_cat_sorted = sorted(cities_in_cat.items(), key=operator.itemgetter(0))
        # sorting dict by key

        return cities_in_cat_sorted

    def get_counties(self):
        """get counties
        return: list of counties"""

        counties = list()
        for city in self.list_of_cities:
            if city.type_of_city == 'powiat' and city.city_name not in counties:
                counties.append([city.type_of_city, city.pow])

        return counties

    def get_county_name_by_id(self, id):
        """get countie name
        return: list of counties"""

        for county in self.list_of_cities:
            if id == county.pow and county.gmi == '':
                return county.city_name

    def get_cities_from_pow(self, id):
        """get cities from pow
        args: id of pow
        Returns: list of cities from pow"""

        list_of_cities = list()
        for city in self.list_of_cities:
            if id == city.pow and city.gmi != '':
                list_of_cities.append(city.city_name)

        return list_of_cities

    def count_counties_with_communities(self):
        """ count communities in counties
        Returns: list of counites
        """
        county_list = list()

        for county in self.get_counties():
            county_list.append([self.get_county_name_by_id(county[1]), len(self.get_cities_from_pow(county[1]))])

        return sorted(county_list[:10], key=operator.itemgetter(1), reverse=True)

    def search_by_name(self, name):
        """get list of cities containing name
        Returns: list of cities
        """
        cities_list = list()
        for city in self.list_of_cities:
            if name.lower() in city.city_name.lower():
                cities_list.append([city.city_name, city.type_of_city])

        return sorted(cities_list, key=operator.itemgetter(0, 1))

    def get_tree_structure(self):
        """get zones by pow"""

        list_of_tree = list()
        for tree in self.list_of_cities:
            list_of_tree.append([tree.pow, tree.gmi, tree.rgmi, tree.city_name, tree.type_of_city])

        return sorted(list_of_tree, key=operator.itemgetter(0, 1, 3))

    def get_nice_tree(self):
        """get nice tree"""

        tree = str()
        current = str()
        deep = 0
        step = 6 * ' '

        for item in self.get_tree_structure():

            if item[0] == '' and item[1] =='' and item[2] =='':
                deep = 0
                tree += step * deep  #if gmi and rgmi == 0

            if item[0] != '' and item[1] =='' and item[2] =='':
                deep = 1
                tree += step * deep#if gmi and rgmi == 0

            if item[0] != '' and item[1] !='' and item[2] !='':
                deep = 2
                tree += step * deep #if gmi and rgmi == 0



            #check current title
            if current != item[4]:
                deep = 2
                if item[0] == '' and item[1] =='' and item[2] =='':
                    deep = 0

                tree +=  '+ (' + item[4] + ')\n' +step * deep
                deep += 1

            tree += '   ' + item[3]
            tree += '\n'

            current = item[4] #current deep
            if item[3] == '':
                deep = 0

        return tree

    @classmethod
    def load_from_file(cls, file):
        """load cities from CSV and create objects"""

        list_of_cities = common.read_file(file)
        list_of_objects_cities = list()

        for city in list_of_cities:
            list_of_objects_cities.append(City(*city[1:]))

        return cls(list_of_objects_cities)


class City:

    def __init__(self, pow, gmi, rgmi, city_name, type_of_city):
        self.pow = pow
        self.gmi = gmi
        self.rgmi = rgmi
        self.city_name = city_name
        self.type_of_city = type_of_city
