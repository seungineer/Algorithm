select animal_type, count(*) as count
from animal_ins
where animal_type like 'Cat' or animal_type like 'Dog'
group by animal_type
order by 1 asc