
def city_function(country, city, population=''):
    if population:
        return country.title() + ',' + city.title() + '-' + population
    else:
        return country.title() + ',' + city.title()


if __name__ == "__main__":
    city_str = city_function("chile", "santiago", "5000")
    print(city_str)
