select u.user_id, nickname, total_sales
from USED_GOODS_USER as u
join 
(select WRITER_ID, sum(PRICE) as total_sales
from USED_GOODS_BOARD
where STATUS = 'DONE'
group by WRITER_ID) as s
on u.USER_ID = s.WRITER_ID
where total_sales >= 700000
order by 3 asc