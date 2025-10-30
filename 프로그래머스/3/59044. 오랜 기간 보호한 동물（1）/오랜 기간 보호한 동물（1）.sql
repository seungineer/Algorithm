select i.name, i.datetime
from animal_ins as i
left outer join animal_outs as o
on i.animal_id = o.animal_id
where o.animal_id is null
order by 2 asc
limit 3