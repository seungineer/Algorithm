-- 리뷰를 가장 많이 작성한 멤버id 서브쿼리
-- 서브쿼리에 rest_review join on member_id
select P.MEMBER_NAME, R.REVIEW_TEXT, date_format(R.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from REST_REVIEW as R
join MEMBER_PROFILE as P
on R.MEMBER_ID = P.MEMBER_ID
where R.MEMBER_ID IN
(select MEMBER_ID
from REST_REVIEW
group  by MEMBER_ID
having count(*) = 
(select count(*)
 from REST_REVIEW
 group by MEMBER_ID
 order by 1 desc
 limit 1))
 order by 3 asc, 2 asc