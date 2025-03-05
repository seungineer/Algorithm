select I.ITEM_ID, I.ITEM_NAME, I.RARITY
from ITEM_TREE as T
left join ITEM_INFO as I
on I.ITEM_ID = T.ITEM_ID
where T.PARENT_ITEM_ID IN (
                            select distinct ITEM_ID
                            from ITEM_INFO
                            where RARITY like 'RARE')
order by 1 desc