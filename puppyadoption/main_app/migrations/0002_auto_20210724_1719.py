# Generated by Django 3.2.5 on 2021-07-24 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='puppies_list',
            name='name',
        ),
        migrations.AddField(
            model_name='puppies_list',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='puppies_list',
            name='breed',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AddField(
            model_name='puppies_list',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='main_app.customer'),
        ),
    ]
