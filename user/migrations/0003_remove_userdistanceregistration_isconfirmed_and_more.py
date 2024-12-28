# Generated by Django 4.2.16 on 2024-12-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_eventlike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdistanceregistration',
            name='isConfirmed',
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='dateOfBirth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='emergencyContactName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='emergencyContactPhone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='firstName',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='firstNameEng',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='lastName',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='lastNameEng',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='phoneNumber',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='sportsClub',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userdistanceregistration',
            name='tShirtSize',
            field=models.CharField(choices=[('XXS', 'Very Extra Small'), ('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large'), ('XXXL', 'Very Extra Extra Large')], max_length=5, null=True),
        ),
    ]