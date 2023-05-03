# Generated by Django 4.1.7 on 2023-05-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0006_alter_orderinfo_order_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goodsinfo",
            name="g_humidity",
            field=models.FloatField(default=85, null=True, verbose_name="储存湿度"),
        ),
        migrations.AlterField(
            model_name="goodsinfo",
            name="g_tempreture",
            field=models.FloatField(default=5, null=True, verbose_name="储存温度"),
        ),
    ]
