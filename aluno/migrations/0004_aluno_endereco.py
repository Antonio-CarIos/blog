# Generated by Django 5.1 on 2024-08-31 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_alter_aluno_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='endereco',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
