select COUNT(*) as FISH_COUNT, MONTH(TIME) as MONTH
from FISH_INFO
group by MONTH(TIME)
order by 2 asc