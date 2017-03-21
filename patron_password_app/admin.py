from django.contrib import admin
from patron_password_app.models import Patron, GoogleAccount, YahooAccount, HotmailAccount, OtherAccount
# Register your models here.

admin.site.register(Patron)
admin.site.register(GoogleAccount)
admin.site.register(YahooAccount)
admin.site.register(HotmailAccount)
admin.site.register(OtherAccount)
