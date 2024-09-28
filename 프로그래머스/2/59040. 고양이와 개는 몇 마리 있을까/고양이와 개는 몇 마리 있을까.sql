select ANIMAL_TYPE, count(*) as count
from ANIMAL_INS
where ANIMAL_TYPE IN ('Cat', 'Dog')
group by ANIMAL_TYPE
order by 1 asc