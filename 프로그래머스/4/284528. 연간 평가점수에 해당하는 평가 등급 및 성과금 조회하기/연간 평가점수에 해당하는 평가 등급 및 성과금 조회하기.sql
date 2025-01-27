select G.EMP_NO, D.EMP_NAME, case when G.SCORE >= 96 then 'S'
    when G.SCORE >= 90 then 'A'
    when G.SCORE >= 80 then 'B'
    else 'C'
    end as GRADE,
    case when G.SCORE >= 96 then D.SAL * 0.2
    when G.SCORE >= 90 then D.SAL * 0.15
    when G.SCORE >= 80 then D.SAL * 0.1
    else D.SAL * 0
    end as BONUS
from (
    select H.EMP_NO, avg(H.SCORE) as SCORE
    from HR_GRADE as H
    group by H.EMP_NO) as G
left join
HR_EMPLOYEES as D
on G.EMP_NO = D.EMP_NO
order by 1 asc