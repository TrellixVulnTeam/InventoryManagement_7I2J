# Generated by Django 2.2.12 on 2020-04-20 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InvManage', '0024_productfiltercolumn_productfilterstate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfiltercolumn',
            old_name='order',
            new_name='position',
        ),
    ]
