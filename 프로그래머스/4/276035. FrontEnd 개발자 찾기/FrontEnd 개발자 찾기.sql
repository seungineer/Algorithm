select distinct D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
from DEVELOPERS as D
join SKILLCODES as S
on S.CODE = D.SKILL_CODE & S.CODE
where S.CATEGORY like 'Front End'
order by 1 asc