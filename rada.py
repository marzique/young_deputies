from rada_helpers import laws_by_deputy

petro_id = 2273 # HETMAN
vakarchuk_id = 11120 

print(f'Законопроектів Порошенко Петра Олексійовича: {laws_by_deputy(petro_id)}')
print(f'Законопроектів Вакарчука Святослава Івановича: {laws_by_deputy(vakarchuk_id)}')
