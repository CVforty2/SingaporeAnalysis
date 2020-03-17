import matplotlib.pyplot as plt
from parsed_data import Data
from matplotlib import cm

if __name__ == "__main__":
    while True:
        year = input("Year: ")
        level = input("Level: ")

        data = Data("/Users/cooperwright/Desktop/Singapore_Analysis/data/"
        "singapore-residents-by-age-group-ethnic-group-and-sex-end-june-annual.csv", year, level)

        # print(data._colors)
        plt.rcParams.update({"font.size": 8})
        fig1, ax1 = plt.subplots()
        ax1.pie(data.sizes, labels=data.labels, colors=data.colors, autopct='%1.1f%%', pctdistance=0.8, shadow=True, startangle=90)
        ax1.axis("equal")
        ax1.set_title(f"{data.year}: {data.level}")
        plt.show()
