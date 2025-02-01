set @all := (select count(*)
             from USER_INFO
             where JOINED LIKE '2021%');

select YEAR(SALES_DATE) as YEAR,
    MONTH(SALES_DATE) as MONTH,
    count(distinct USER_ID) as PURCHASED_USERS,
    round(count(distinct USER_ID) / @all, 1) as PURCHASED_RATIO
from ONLINE_SALE
where USER_ID in (select USER_ID
             from USER_INFO
             where JOINED LIKE '2021%'
            )
group by YEAR, MONTH
order by 1, 2 asc