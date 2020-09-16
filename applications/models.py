from django.db import models
import uuid


class TypesOfPayment(models.TextField):
    pass


class Application(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4)
    number = models.CharField(max_length=200)
    date = models.DateTimeField()
    partner = models.CharField(max_length=200)
    summ = models.DecimalField(max_digits=10, decimal_places=2)
    initiator = models.CharField(max_length=200)
    current_state = models.CharField(max_length=200)
    pay_before = models.DateField()
    type_of_payment = models.CharField(max_length=50)

    def __str__(self):
        return f'Заявка на расходование ДС {self.number} от {self.date}'
