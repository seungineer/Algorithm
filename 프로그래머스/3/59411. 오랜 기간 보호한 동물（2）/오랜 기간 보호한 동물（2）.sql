select O.ANIMAL_ID, O.NAME
from ANIMAL_OUTS as O
inner join ANIMAL_INS as I
on O.ANIMAL_ID = I.ANIMAL_ID
order by O.DATETIME - I.DATETIME desc
limit 2