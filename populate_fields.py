import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'patron_password_manager.settings')

import django
django.setup()

## FAKE POP SCRIPT

import random
from patron_password_app.models import Patron, GoogleAccount, YahooAccount, HotmailAccount, OtherAccount
from faker import Faker



fakegen = Faker()


def add_patron(N=5):

    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_phone = fakegen.phone_number()
        fake_card = '10001' + fakegen.ean(length=8)

        patron_maker = Patron.objects.get_or_create(first_name=fake_first_name, last_name = fake_last_name,
                                                    phone_number = fake_phone, library_card_number = fake_card)

        print(Patron.objects.count())


def add_accounts():
    for patron in Patron.objects.all():
        if bool(random.getrandbits(1)):
            fake_user = fakegen.user_name()
            fake_password = fakegen.password(length=6)
            google_maker = GoogleAccount.objects.get_or_create(patron=patron, username=fake_user,
                                                               password=fake_password)
        if bool(random.getrandbits(1)):
            fake_user = fakegen.user_name()
            fake_password = fakegen.password(length=6)
            yahoo_maker = YahooAccount.objects.get_or_create(patron=patron, username=fake_user,
                                                               password=fake_password)
        if bool(random.getrandbits(1)):
            fake_user = fakegen.user_name()
            fake_password = fakegen.password(length=6)
            hotmail_maker = HotmailAccount.objects.get_or_create(patron=patron, username=fake_user,
                                                               password=fake_password)
        if bool(random.getrandbits(1)):
            fake_user = fakegen.user_name()
            fake_password = fakegen.password(length=6)
            fake_service = fakegen.company()
            other_maker = OtherAccount.objects.get_or_create(patron=patron, service=fake_service, username=fake_user,
                                                               password=fake_password)

if __name__ == '__main__':
    print("populating script!")
    add_patron(50)
    add_accounts()
    print("Populating complete!")
