# Generated by Django 4.1.7 on 2023-05-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0008_alter_warehouseinfo_wh_loc"),
    ]

    operations = [
        migrations.AddField(
            model_name="goodsinfo",
            name="g_production_time",
            field=models.DateField(blank=True, null=True, verbose_name="生产日期"),
        ),
        migrations.AlterField(
            model_name="goodsinfo",
            name="g_category",
            field=models.CharField(blank=True, max_length=16, verbose_name="货物种类"),
        ),
        migrations.AlterField(
            model_name="goodsinfo",
            name="g_life",
            field=models.DateField(blank=True, verbose_name="保质期"),
        ),
        migrations.AlterField(
            model_name="goodsinfo",
            name="g_name",
            field=models.CharField(blank=True, max_length=16, verbose_name="货物名称"),
        ),
        migrations.AlterField(
            model_name="goodsinfo",
            name="g_vendor",
            field=models.CharField(blank=True, max_length=16, verbose_name="供应商"),
        ),
    ]
