select I.ITEM_ID, I.ITEM_NAME, I.RARITY
from ITEM_INFO as I
left join (
    select *, 0 as VISIBLE
    from ITEM_INFO
    where ITEM_ID IN (
        select PARENT_ITEM_ID
        from ITEM_TREE)) as P
on I.ITEM_ID = P.ITEM_ID
where ISNULL(P.VISIBLE)
order by 1 desc