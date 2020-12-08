# Generated by Django 2.2.6 on 2020-01-19 17:03

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_auto_20200115_2119'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='presenter',
            managers=[
                ('speakers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='presenters',
        ),
        migrations.AddField(
            model_name='activity',
            name='presenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.Presenter'),
        ),
    ]
