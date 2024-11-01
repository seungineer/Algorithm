select P.PRODUCT_ID, P.PRODUCT_NAME, SUM(A.AMOUNT * P.PRICE) as TOTAL_SALES
from (
    select PRODUCT_ID, AMOUNT
    from FOOD_ORDER
    where PRODUCE_DATE LIKE '2022-05%') as A
join FOOD_PRODUCT as P
on A.PRODUCT_ID = P.PRODUCT_ID
group by A.PRODUCT_ID
order by 3 desc, 1 asc