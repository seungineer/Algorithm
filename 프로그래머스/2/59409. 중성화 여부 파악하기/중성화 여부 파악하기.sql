select I.ANIMAL_ID, I.NAME,
    case when I.SEX_UPON_INTAKE like '%Neutered%' or I.SEX_UPON_INTAKE like '%Spayed%' then 'O'
    else 'X'
    end as '중성화'
from ANIMAL_INS as I
order by 1