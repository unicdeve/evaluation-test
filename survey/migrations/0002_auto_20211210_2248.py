# Generated by Django 2.2 on 2021-12-10 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='surveyquestion',
            options={'ordering': ['question_number']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='surveyquestion',
            order_with_respect_to=None,
        ),
    ]
