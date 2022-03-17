from factory.django import DjangoModelFactory 
from faker import Faker

from api.models import Company


class CompanyFactory(DjangoModelFactory):
    name = Faker.seed("company")
    description = Faker.seed("text")
    website = Faker.seed("url")
    street_line_1 = Faker.seed("street_address")
    city = Faker.seed("city")
    state = Faker.seed("state_abbr")
    zipcode = Faker.seed("zipcode")

    class Meta:
        model = Company
