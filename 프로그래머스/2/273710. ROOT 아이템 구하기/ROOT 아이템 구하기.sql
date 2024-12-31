select I.ITEM_ID, I.ITEM_NAME
from ITEM_INFO as I
left join  ITEM_TREE as T
on I.ITEM_ID = T.ITEM_ID
where ISNULL(T.PARENT_ITEM_ID)
order by 1 asc