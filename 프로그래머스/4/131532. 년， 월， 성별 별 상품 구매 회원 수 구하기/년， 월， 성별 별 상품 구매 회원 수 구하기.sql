select YEAR(O.SALES_DATE) as YEAR, MONTH(O.SALES_DATE) as MONTH, S.GENDER as GENDER, count(distinct S.USER_ID) as USERS
from ONLINE_SALE as O
inner join (
    select *
    from USER_INFO as UI
    where NOT ISNULL(UI.GENDER)) as S
on S.USER_ID = O.USER_ID
group by YEAR, MONTH, GENDER
order by 1, 2, 3 asc