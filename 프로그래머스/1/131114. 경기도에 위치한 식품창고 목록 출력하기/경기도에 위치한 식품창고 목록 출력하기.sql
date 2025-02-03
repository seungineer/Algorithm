select W.WAREHOUSE_ID, W.WAREHOUSE_NAME, W.ADDRESS, case when ISNULL(W.FREEZER_YN) then 'N'
                                                        else W.FREEZER_YN
                                                        end as FREEZER_YN
from FOOD_WAREHOUSE as W
where W.ADDRESS like '경기도%'
order by 1 asc