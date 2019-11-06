from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import os


class Deputy(models.Model):
    rada_id = models.IntegerField()
    name = models.CharField(max_length=200) # "Порошенко Петро "
    submitted_laws = models.IntegerField()
    photo = models.CharField(max_length=200)
    monitoring = models.IntegerField()
    attendance = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)]) 
    last_month_position = models.IntegerField()
    position_current = models.IntegerField()
    rating_upfoundation = models.IntegerField()
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
        (OPZZH, 'ОПОЗИЦІЙНА ПЛАТФОРМА - ЗА ЖИТТЯ'),
        (BATKIVSHYNA, 'Батьківщина'),
        (E_SOLIDARNIST, 'Європейська Солідарність'),
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
        difference =  self.last_month_position - self.position_current
        if difference > 0:
            return f'<span class="difference positive">(+{difference})<i class="fas fa-long-arrow-alt-up"></i></span>'
        elif difference < 0:
            return f'<span class="difference negative">({difference})<i class="fas fa-long-arrow-alt-down"></i></span>'
        else:
            return '<span class="difference null">(-)</span>'
    
    def name_surname(self):
        splitted = self.name.split(' ')
        return ' '.join(splitted[:2][::-1])

    def attendance_to_degrees(self):
        """Scale 100% percentage to 180 degrees"""
        return self.attendance * 1.8
