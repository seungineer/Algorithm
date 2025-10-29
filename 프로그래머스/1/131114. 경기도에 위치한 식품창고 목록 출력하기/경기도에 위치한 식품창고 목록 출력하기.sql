select warehouse_id, warehouse_name, address, if(isnull(freezer_yn), 'N', freezer_yn) as freezer_yn
from food_warehouse
where address like '경기도%'
order by 1 asc