# Generated by Django 4.2.4 on 2023-08-28 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_alter_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='evolution',
        ),
        migrations.AddField(
            model_name='post',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_pokemon', to='pokemon_entities.post', verbose_name='Эволюционировал из'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
