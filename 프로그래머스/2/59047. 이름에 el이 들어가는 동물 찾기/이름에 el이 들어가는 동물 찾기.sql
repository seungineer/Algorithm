select I.ANIMAL_ID, I.NAME
from ANIMAL_INS as I
where I.ANIMAL_TYPE like 'Dog' and lower(I.NAME) like '%el%'
order by 2