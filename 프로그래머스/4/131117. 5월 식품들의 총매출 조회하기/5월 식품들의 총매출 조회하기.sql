select A.PRODUCT_ID, A.PRODUCT_NAME, SUM(A.PRICE * B.AMOUNT) as TOTAL_SALES
from FOOD_PRODUCT as A
join (select *
      from FOOD_ORDER
      where PRODUCE_DATE LIKE '2022-05%'
     ) as B
on A.PRODUCT_ID = B.PRODUCT_ID
group by A.PRODUCT_ID
order by 3 desc, 1 asc