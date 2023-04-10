# Generated by Django 4.1.7 on 2023-04-10 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя заказчика')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
            ],
        ),
        migrations.CreateModel(
            name='TagCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ManyToManyField(to='cloth.tagcl')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='OrderCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('На обработке', 'На обработке'), ('Выехал', 'Выехал'), ('Отправлен', 'Отправлен')], max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloth.customercl')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloth.productcl')),
            ],
        ),
    ]
