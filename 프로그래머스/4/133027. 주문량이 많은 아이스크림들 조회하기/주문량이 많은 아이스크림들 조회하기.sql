select H.FLAVOR
from (select *, sum(total_order) as total_half
      from FIRST_HALF
      group by FLAVOR) as H
join
      (select *, sum(total_order) as total_july
       from JULY
       group by FLAVOR) as J
on H.FLAVOR = J.FLAVOR
order by J.total_july + H.total_half desc
limit 3