select count(*) as FISH_COUNT, N.FISH_NAME
from FISH_INFO as F
left join FISH_NAME_INFO as N
on F.FISH_TYPE = N.FISH_TYPE
group by N.FISH_NAME
order by 1 desc