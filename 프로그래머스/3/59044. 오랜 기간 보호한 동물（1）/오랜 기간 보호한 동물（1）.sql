select I.NAME, I.DATETIME
from ANIMAL_INS as I
left join ANIMAL_OUTS as O
on I.ANIMAL_ID = O.ANIMAL_ID
where O.ANIMAL_ID IS NULL
order by I.DATETIME asc
limit 3