-- 카테고리와 프라이스가 서브쿼리에 있는지 확인
-- 카테고리 별로 가장 비싼 가격 서브 쿼리
-- 카테고리 중 제시된 것인지 확인
SELECT category, price AS MAX_PRICE, product_name
FROM FOOD_PRODUCT
WHERE (category, price) IN (SELECT category, MAX(PRICE)
FROM FOOD_PRODUCT
group by category) AND
category IN ('과자', '국', '김치', '식용유')
order by 2 desc