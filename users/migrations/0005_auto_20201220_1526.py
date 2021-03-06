# Generated by Django 3.1.3 on 2020-12-20 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goldenMedal', models.BooleanField(default=False)),
                ('gto', models.BooleanField(default=False)),
                ('volunteering', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='achievements',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.achievements'),
        ),
    ]
