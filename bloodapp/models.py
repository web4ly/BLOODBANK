from django.db import models

class Donor(models.Model):
    donor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    registration_date = models.DateField()

    class Meta:
        db_table = 'Donor'

class Recipient(models.Model):
    recipient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    registration_date = models.DateField()

    class Meta:
        db_table = 'Recipient'

class BloodStock(models.Model):
    bloodstock_id = models.AutoField(primary_key=True)
    blood_group = models.CharField(max_length=3)
    quantity = models.IntegerField()
    last_update_date = models.DateField()

    class Meta:
        db_table = 'BloodStock'

class Donation(models.Model):
    donation_id = models.AutoField(primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donation_date = models.DateField()
    blood_group = models.CharField(max_length=3)

    class Meta:
        db_table = 'Donation'

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    blood_group = models.CharField(max_length=3)

    class Meta:
        db_table = 'Transaction'

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'Admin'
