select MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from REST_REVIEW as R
join MEMBER_PROFILE as P
on R.MEMBER_ID = P.MEMBER_ID
where P.MEMBER_ID IN
(select MEMBER_ID
from REST_REVIEW as R
group by R.MEMBER_ID
having count(*) = (
select MAX(CNT) as MAX_CNT
from(
select count(*) as CNT
from REST_REVIEW as R
group by R.MEMBER_ID)as RR))
order by 3 asc, 2 asc