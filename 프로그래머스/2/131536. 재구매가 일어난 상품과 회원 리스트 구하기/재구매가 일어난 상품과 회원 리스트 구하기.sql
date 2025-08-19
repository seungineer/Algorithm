select sub.user_id, sub.product_id
from (
    select user_id, product_id, count(*) as cnt
    from online_sale
    group by user_id, product_id
) as sub
where sub.cnt > 1
order by 1 asc, 2 desc