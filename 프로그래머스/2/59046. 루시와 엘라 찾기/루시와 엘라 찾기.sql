select I.ANIMAL_ID, I.NAME, I.SEX_UPON_INTAKE
from ANIMAL_INS as I
where I.NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by 1