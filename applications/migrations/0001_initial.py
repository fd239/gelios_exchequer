# Generated by Django 3.1.1 on 2020-09-15 13:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('number', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('partner', models.CharField(max_length=200)),
                ('summ', models.DecimalField(decimal_places=2, max_digits=10)),
                ('initiator', models.CharField(max_length=200)),
                ('current_state', models.CharField(max_length=200)),
                ('pay_before', models.DateField()),
                ('type_of_payment', models.CharField(max_length=50)),
            ],
        ),
    ]
