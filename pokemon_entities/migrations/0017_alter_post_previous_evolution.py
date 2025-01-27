# Generated by Django 4.2.4 on 2023-09-01 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_alter_pokemonentity_attack_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.post', verbose_name='Эволюционировал из'),
        ),
    ]
