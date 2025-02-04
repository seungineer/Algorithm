select date_format(N.SALES_DATE, '%Y-%m-%d') as SALES_DATE, N.PRODUCT_ID, N.USER_ID, N.SALES_AMOUNT
from ONLINE_SALE as N
where N.SALES_DATE like '2022-03%'
union
select date_format(F.SALES_DATE, '%Y-%m-%d') as SALES_DATE, F.PRODUCT_ID, NULL as USER_ID, F.SALES_AMOUNT
from OFFLINE_SALE as F
where F.SALES_DATE like '2022-03%'
order by 1, 2, 3 asc

