from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import os


class Deputy(models.Model):
    rada_id = models.IntegerField()
    name = models.CharField(max_length=200)
    name_ukr = models.CharField(max_length=200)
    upr = models.IntegerField() # UPR
    experts = models.IntegerField()
    monitoring = models.IntegerField() # SMI
    submitted_laws = models.IntegerField()
    photo = models.CharField(max_length=200)
    last_month_position = models.IntegerField()
    position_current = models.IntegerField()
    txt_for_page = models.TextField(max_length=2500)

    SLUGA_NARODU = 'SN'
    OPZZH = 'OP'
    BATKIVSHYNA = 'BT'
    E_SOLIDARNIST = 'ES'
    HOLOS = 'HL'
    ZA_MAIBUTNIE = 'ZM'
    BEZ_PARTII = 'BP'
    PARTIES = [
        (SLUGA_NARODU, 'Слуга Народу'),
        (OPZZH, 'ОПЗЖ'),
        (BATKIVSHYNA, 'Батьківщина'),
        (E_SOLIDARNIST, 'ЄС'),
        (HOLOS, 'Голос'),
        (ZA_MAIBUTNIE, 'За майбутнє'),
        (BEZ_PARTII, 'Позафракційні'),
    ]

    party = models.CharField(
        max_length=200,
        choices=PARTIES,
        default=BEZ_PARTII,
    )

    def __str__(self):
        return self.name
    
    def position_change(self):
        return self.last_month_position - self.position_current

    def position_change_snippet(self):
        difference = self.position_change()
        if difference > 0:
            return f'<span class="difference positive">(+{difference})<i class="fas fa-long-arrow-alt-up"></i></span>'
        elif difference < 0:
            return f'<span class="difference negative">({difference})<i class="fas fa-long-arrow-alt-down"></i></span>'
        else:
            return '<span class="difference null">(-)</span>'
    
    def name_surname(self):
        splitted = self.name.split(' ')
        return ' '.join(splitted[:2][::-1])
    
    def surname(self):
        splitted = self.name.split(' ')
        return splitted[0]
    
    def surname_ukr(self):
        splitted = self.name_ukr.split(' ')
        return splitted[0]

    def votes(self):
        return self.uniqueuser_set.count()


class UniqueUser(models.Model):
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    deputies = models.ManyToManyField(Deputy)

    def __str__(self):
        return self.ip
