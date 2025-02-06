select left(P.PRODUCT_CODE, 2) as CATEGORY, count(*) as PRODUCTS
from PRODUCT as P
group by CATEGORY
order by 1 asc