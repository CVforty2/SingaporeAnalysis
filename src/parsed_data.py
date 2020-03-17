import random

class Data:

    def __init__(self, filename, year, level):
        self.filename = filename
        self.year = str(year)
        self.level = level
        self._year_data = {}
        self._labels = []
        self._colors = []
        self._sizes = []
        self.parse()
        self.random_colors()
        self.wedge_sizes()


    def parse(self):
        with open(self.filename) as data:
            for line in data:
                _year, _level, _age_range, _value = line.split(',')
                if self.year == _year and self.level == _level:
                    if "Over" not in _age_range:
                        if _value == "na\n":
                            _value = "0"
                        self._year_data[_age_range] = int(_value)
            self._labels = sorted(self._year_data.keys())


    def random_colors(self):
        for i in range(10):
            hex_aphabet = "0123456789abcdef"
            rgb_string = "#"
            for i in range(6):
                random_int = random.randrange(len(hex_aphabet))
                rgb_string += hex_aphabet[random_int]
            self._colors.append(rgb_string)


    def wedge_sizes(self):
        total = sum(self._year_data.values())
        summed_proportion = 0.0
        for i in sorted(self._year_data.keys()):
            proportion = self._year_data[i] / total
            if proportion <= 0.03:
                self._labels.remove(i)
                summed_proportion += proportion
            else:
                self._sizes.append(self._year_data[i] / total)
        if summed_proportion != 0.0:
            self._labels.append("Others")
            self._sizes.append(summed_proportion)



    def get_labels(self):
        return self._labels

    def get_colors(self):
        return self._colors

    def get_sizes(self):
        return self._sizes


    labels = property(get_labels)

    colors = property(get_colors)

    sizes = property(get_sizes)




if __name__ == "__main__":
    x = Data("test", 1980, "Total Residents")
    x.get_colors()
    print(x._colors)
