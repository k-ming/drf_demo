# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Flower(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.TextField()
    height = models.IntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    bust = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    habit = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flower'
