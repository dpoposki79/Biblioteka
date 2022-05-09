from .models import Clenovi
from django.utils.timezone import now
from twilio.rest import Client

def send_sms():
    clenovi = Clenovi.objects.all()
    account_sid = "ACaebe3d2e823f88628bef969cb4c4441e"
    auth_token = "ab6e42598abc29fb68ac5100e4acea6f"
    client = Client(account_sid, auth_token)
    for clen in clenovi:
        denovi_pozajmena = (now() - clen.Data_pozajmuvanje).days
        denovi_potsetuvanje = clen.Denovi_potsetuvanje
        if denovi_pozajmena == denovi_potsetuvanje:
            client.messages \
            .create(
                body="Pocituvan {}, ve molime vratete ja knigata {} koja e pozajmena na {}." . format(clen.Ime, clen.Pozajmena_kniga.Naslov, clen.Data_pozajmuvanje),
                from_='+19894364685',
                to=clen.Telefon
    )