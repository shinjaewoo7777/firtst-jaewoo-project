class Country:
    def __init__(self, country_name, population):
        self.country_name = country_name
        self.population = population

    def display(self):
        print('국가명: %s, 인구수: %d' % (self.country_name, self.population))


class Newcountry(Country):
    def __init__(self, country_name, population, capital):
        super().__init__(country_name, population)
        self.capital = capital

    def display(self):
        print('국가명: %s, 인구수: %d, 수도명: %s' % (self.country_name, self.population, self.capital))


aCountry = Country('Korea', 5000)
bCountry = Newcountry('NewWorld', 5000, 'Seoul')

aCountry.display()
bCountry.display()