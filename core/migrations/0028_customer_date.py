# Generated by Django 5.0.3 on 2024-04-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_faq_faqsettings_faqquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
