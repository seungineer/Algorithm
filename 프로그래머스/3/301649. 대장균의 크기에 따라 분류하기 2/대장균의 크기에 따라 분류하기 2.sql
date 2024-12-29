select ORG.ID, case
                 when ORG.QUARTILE = 1 then 'LOW'
                 when ORG.QUARTILE = 2 then 'MEDIUM'
                 when ORG.QUARTILE = 3 then 'HIGH'
                 when ORG.QUARTILE = 4 then 'CRITICAL'
                end as COLONY_NAME
from (select *,
      NTILE(4) OVER (ORDER BY SIZE_OF_COLONY) as QUARTILE
      from ECOLI_DATA) as ORG
order by 1 asc