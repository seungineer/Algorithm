select ANIMAL_ID, ANIMAL_TYPE, NAME
from ANIMAL_OUTS
where ANIMAL_ID IN
                  (select ANIMAL_ID
                   from ANIMAL_INS
                   where SEX_UPON_INTAKE LIKE 'Intact%')
      and (SEX_UPON_OUTCOME LIKE'Spayed%' or
           SEX_UPON_OUTCOME LIKE'Neutered%')