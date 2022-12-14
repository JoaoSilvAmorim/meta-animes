# Generated by Django 4.1.2 on 2022-10-08 17:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('animes_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'animes',
            },
        ),
        migrations.AlterField(
            model_name='chapters',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
