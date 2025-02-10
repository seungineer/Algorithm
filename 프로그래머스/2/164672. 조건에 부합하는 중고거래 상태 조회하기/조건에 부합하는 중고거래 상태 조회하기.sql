select BOARD_ID, WRITER_ID, TITLE, PRICE, case when STATUS like 'DONE' then '거래완료'
                when STATUS like 'SALE' then '판매중'
                when STATUS like 'RESERVED' then '예약중'
                else NULL end as STATUS
from USED_GOODS_BOARD
where date_format(CREATED_DATE, '%Y-%m-%d') like '2022-10-05'
order by 1 desc