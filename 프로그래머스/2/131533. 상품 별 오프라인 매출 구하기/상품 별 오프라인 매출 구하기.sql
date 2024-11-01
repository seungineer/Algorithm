select P.PRODUCT_CODE, SUM(S.SALES_AMOUNT * P.PRICE) as SALES
from OFFLINE_SALE as S
left join PRODUCT as P
on S.PRODUCT_ID = P.PRODUCT_ID
group by P.PRODUCT_CODE
order by 2 desc, 1 asc