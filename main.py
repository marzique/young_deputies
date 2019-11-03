from rada.scraper import laws_by_deputy, name_by_id

petro_id = 2273 # HETMAN
# vakarchuk_id = 11120 

print(f'{name_by_id(petro_id)} подав {laws_by_deputy(petro_id)} законопроектів')
