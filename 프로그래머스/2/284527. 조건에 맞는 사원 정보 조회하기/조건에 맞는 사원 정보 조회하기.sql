select sum(G.SCORE) as SCORE, G.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
from HR_GRADE as G
left join HR_EMPLOYEES as E
on G.EMP_NO = E.EMP_NO
group by G.EMP_NO
order by 1 desc
limit 1