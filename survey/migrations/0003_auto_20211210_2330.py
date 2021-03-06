# Generated by Django 2.2 on 2021-12-10 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20211210_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestion',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.Survey'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_surveys', to=settings.AUTH_USER_MODEL),
        ),
    ]
