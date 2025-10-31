select f.flavor
from (
    select flavor, sum(total_order) as tot
    from july
    group by flavor
) as f
inner join first_half as h
on f.flavor = h.flavor
order by f.tot + h.total_order desc
limit 3