select D.QUARTER, count(*) as ECOLI_COUNT
from (
    select *, case when MONTH(DIFFERENTIATION_DATE) <= 3 then '1Q'
                    when MONTH(DIFFERENTIATION_DATE) <= 6 then '2Q'
                    when MONTH(DIFFERENTIATION_DATE) <= 9 then '3Q'
                    when MONTH(DIFFERENTIATION_DATE) <= 12 then '4Q'
                    else NULL end as QUARTER
    from ECOLI_DATA) as D
group by D.QUARTER
order by 1