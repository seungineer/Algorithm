select P.product_code, A.total_amount * P.price as sales
from PRODUCT as P
join  (select PRODUCT_ID, SUM(sales_amount) as total_amount
       from OFFLINE_SALE
       group by PRODUCT_ID) as A
on P.PRODUCT_ID = A.PRODUCT_ID
order by 2 desc, 1 asc