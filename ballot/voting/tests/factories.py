from factory import django, Faker

from voting.models import Voter


class VoterFactory(django.DjangoModelFactory):
    class Meta:
        model = Voter

    first_name = Faker('first_name')
    last_name = Faker('last_name')
    dni = Faker('random_int', min=0, max=57000000)
    birth_date = Faker('date_of_birth')
    has_voted = False
