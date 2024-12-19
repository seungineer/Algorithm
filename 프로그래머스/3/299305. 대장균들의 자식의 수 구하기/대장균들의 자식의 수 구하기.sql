select E.ID, IF(ISNULL(S.CHILD_CNT), 0, S.CHILD_CNT) as CHILD_COUNT
from ECOLI_DATA as E
left outer join
                 (select PARENT_ID, count(*) as CHILD_CNT
                 from ECOLI_DATA
                 group by PARENT_ID) as S
on E.ID = S.PARENT_ID
order by 1 asc