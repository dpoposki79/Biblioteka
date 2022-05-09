from django.contrib import admin
from .models import Knigi, Clenovi
from django.utils.timezone import now
from datetime import timedelta
from twilio.rest import Client
import smtplib, ssl

# Register your models here.

@admin.action(description="Notify user by SMS")
def notify_sms(modeladmin, request, queryset):
    account_sid = "ACaebe3d2e823f88628bef969cb4c4441e"
    auth_token = "ab6e42598abc29fb68ac5100e4acea6f"
    client = Client(account_sid, auth_token)
    for user in queryset:
        client.messages \
            .create(
                body="Pocituvan {}, ve molime vratete ja knigata {} koja e pozajmena na {}." . format(user.Ime, user.Pozajmena_kniga.Naslov, user.Data_pozajmuvanje),
                from_='+19894364685',
                to=user.Telefon
    )
@admin.action(description="Notify user by EMAIL")
def notify_email(modeladmin, request, queryset):
    smtp_server = "smtp.mail.ru"
    sender = "tolstyakova-ada@mail.ru"
    pwd = "D4gJfe8NHd5UB8f6510T"
    port = 465
    ssl_conn = ssl.create_default_context()
    for user in queryset:
        body = "Pocituvan {}, ve molime vratete ja knigata {} koja e pozajmena na {}." . format(user.Ime, user.Pozajmena_kniga.Naslov, user.Data_pozajmuvanje)
        with smtplib.SMTP_SSL(smtp_server, port, context=ssl_conn) as server:
            server.login(sender, pwd)
            server.sendmail(sender, user.Email, body) 


class ClenoviAdmin(admin.ModelAdmin):
    @admin.display(ordering="Data_pozajmuvanje", description="Denovi Pozajmena")
    def denovi_pozajmena_kniga(self, obj):
        if obj.Data_pozajmuvanje != None:
            return (now() - obj.Data_pozajmuvanje).days
        else:
            return obj.Dali_ima_pozajmeno

    list_display = ("id", "Ime", "Prezime", "Telefon", "Email", "Data_clenstvo", "Broj_clenska", "Aktiven", "Data_platena_clenarina", "Dali_ima_pozajmeno", "Data_pozajmuvanje", "denovi_pozajmena_kniga")
    list_filter = ("Data_clenstvo", "Data_pozajmuvanje", "Aktiven", "Dali_ima_pozajmeno")
    search_fields = ("Ime", "Prezime")
    actions = (notify_sms, notify_email ) #Da se pojavi na web vo delot akcija


class KnigiAdmin(admin.ModelAdmin):
    list_display = ("id", "Naslov", "Avtor", "Zarn", "Kolicina", "Izdavac", "El_ver", "El_path", "Nabavna_cena")
    list_filter = ("Zarn", "Avtor", "Izdavac")
    search_fields = ("Naslov", "Avtor")


admin.site.register(Knigi, KnigiAdmin)
admin.site.register(Clenovi, ClenoviAdmin)