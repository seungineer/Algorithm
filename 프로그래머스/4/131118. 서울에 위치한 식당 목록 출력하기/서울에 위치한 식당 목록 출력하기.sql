-- 코드를 입력하세요
-- rest_review에서 rest_id에 따라 리뷰 스코어를 평균낸 서브쿼리를 조인하여
-- 필요한 정보 출력
select A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, ROUND(B.avg_score, 2) as SCORE
from REST_INFO as A
JOIN (SELECT REST_ID, AVG(REVIEW_SCORE) as avg_score
      from REST_REVIEW
      group by REST_ID) as B
on A.REST_ID = B.REST_ID
WHERE A.ADDRESS LIKE '서울%'
order by SCORE desc, FAVORITES desc