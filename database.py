# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read
# in any csv file

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


# add in code for a Database class

class DB:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name: object) -> object:
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None


# add in code for a Table class
import copy


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def __is_float(self, element):
        if element is None:
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        # print(self.table)
        for item1 in self.table:
            # print(item1)
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            if self.__is_float(item1[aggregation_key]):
                temps.append(float(item1[aggregation_key]))
            else:
                temps.append(item1[aggregation_key])
        return function(temps)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def insert(self, entry):
        if isinstance(entry, dict):
            self.table.append(entry)
        # Random key 6 if key not in csv then append else genarate new id

    def update(self, key, column, new_value):
        for item in self.table:
            if item[column] == column:
                item[key] = new_value
                break

    def __str__(self):
        return self.table_name + ':' + str(self.table)

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list
# of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with
# a key can be updated
