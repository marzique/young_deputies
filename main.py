from rada.scraper import laws_by_deputy, name_by_id

deputy_id = 21165 
# vakarchuk_id = 11120 

print(f'{name_by_id(deputy_id)} подав {laws_by_deputy(deputy_id)} законопроектів')
