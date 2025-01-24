select GGG.ID
from ECOLI_DATA as GGG
where GGG.PARENT_ID IN (
    select GG.ID
    from ECOLI_DATA as GG
    where GG.PARENT_ID IN (
        select G.ID
        from ECOLI_DATA as G
        where ISNULL(G.PARENT_ID)
        )
    )
order by 1 asc

