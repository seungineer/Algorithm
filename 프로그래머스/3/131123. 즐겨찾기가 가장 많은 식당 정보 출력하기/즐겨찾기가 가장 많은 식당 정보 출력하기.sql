-- 음식종류, max_favorite인 서브쿼리
-- 해당 서브쿼리 내에 포함된 것 출력
-- 음식 종류를 기준으로 내림차순 정렬
select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from REST_INFO
where (FOOD_TYPE, FAVORITES) IN
(select food_type, MAX(favorites)
from REST_INFO
group by food_type)
order by 1 desc