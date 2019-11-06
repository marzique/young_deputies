from .rada.scraper import laws_by_deputy
from .googler.scraper import total_search_results
from .models import Deputy


def refresh_deputies_laws_number():
    """Refresh each deputy's submitted laws variable by scraping it from rada website"""
    deputies = Deputy.objects.all()
    for deputy in deputies:
        deputy.submitted_laws = laws_by_deputy(deputy.rada_id)
        deputy.save()


def refresh_deputies_google_search_number():
    """"""
    deputies = Deputy.objects.all()
    for deputy in deputies:
        deputy.monitoring = total_search_results(deputy.name_surname())
        deputy.save()
