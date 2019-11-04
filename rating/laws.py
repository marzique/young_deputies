from .rada.scraper import laws_by_deputy
from .models import Deputy


def refresh_deputies_laws_number():
    """Refresh each deputy's submitted laws variable by scraping it from rada website"""
    deputies = Deputy.objects.all()
    for deputy in deputies:
        deputy.laws = laws_by_deputy(deputy.rada_id)
        deputy.save()
    # TODO: set some last_updated_value as singleton model in db here

