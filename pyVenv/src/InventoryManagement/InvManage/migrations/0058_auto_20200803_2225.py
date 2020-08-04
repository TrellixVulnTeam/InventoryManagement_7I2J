# Generated by Django 2.2.12 on 2020-08-03 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InvManage', '0057_auto_20200803_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='phone',
        ),
        migrations.AddField(
            model_name='vendor',
            name='bankaccount',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='InvManage.BankAccount'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='communication',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='InvManage.Communication'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='purchasedata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='InvManage.PurchaseData'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='InvManage.ShippingAddress'),
        ),
    ]
