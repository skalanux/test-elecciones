from django.db import models


class Voter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.PositiveIntegerField(unique=True)
    birth_date = models.DateField()
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Voter'
        verbose_name_plural = 'Voters'


class PoliticalParty(models.Model):
    party_number = models.PositiveIntegerField(unique=True)
    party_name = models.CharField(max_length=50)
    president = models.CharField(max_length=100)
    vice_president = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.party_number} - {self.party_name}'

    class Meta:
        verbose_name = 'Political Party'
        verbose_name_plural = 'Political Parties'
