from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):

    def seed_data(apps, schema_editor):
        user = CustomUser(name='name',
                          email='mail@gmail.com',
                          is_active=True,
                          is_staff=True,
                          is_superuser=True,
                          phone='987654321',

                          )
        user.set_password('anypassword')
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
