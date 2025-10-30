select animal_id, name
from (
    select o.animal_id, o.name, i.intake_condition
    from animal_outs as o
    left outer join
    animal_ins as i
    on o.animal_id = i.animal_id) as t
where t.intake_condition is null
order by 1, 2