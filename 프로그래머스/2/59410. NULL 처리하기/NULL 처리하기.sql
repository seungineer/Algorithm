select ANIMAL_TYPE, case when ISNULL(NAME) then "No name"
                        else NAME
                        end as NAME,
    SEX_UPON_INTAKE
from ANIMAL_INS
order by ANIMAL_ID asc