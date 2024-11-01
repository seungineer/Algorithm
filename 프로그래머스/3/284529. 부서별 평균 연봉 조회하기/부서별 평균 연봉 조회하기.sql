select E.DEPT_ID, D.DEPT_NAME_EN, ROUND(AVG(E.SAL)) as AVG_SAL
from HR_EMPLOYEES as E
join HR_DEPARTMENT as D
on E.DEPT_ID = D.DEPT_ID
group by D.DEPT_ID
order by 3 desc