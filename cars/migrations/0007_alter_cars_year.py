# Generated by Django 4.2 on 2023-05-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_car_feature_remove_cars_features_cars_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='year',
            field=models.IntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], verbose_name='year'),
        ),
    ]
