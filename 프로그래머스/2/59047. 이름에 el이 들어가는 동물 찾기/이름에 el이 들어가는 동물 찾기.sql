select I.ANIMAL_ID, I.NAME
from ANIMAL_INS as I
where I.ANIMAL_TYPE like 'Dog' and
    (I.NAME like '%EL%' or
    I.NAME like '%El%' or
    I.NAME like '%eL%' or
    I.NAME like '%el%')
order by 2