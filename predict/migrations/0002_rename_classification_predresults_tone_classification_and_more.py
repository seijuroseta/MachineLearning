from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predresults',
            old_name='classification',
            new_name='tone_classification',
        ),
        migrations.AddField(
            model_name='predresults',
            name='score_classification',
            field=models.CharField(default=5, max_length=30),
            preserve_default=False,
        ),
    ]
