-- 성분 타입에 대한 아이스크림 총 주문량 조회
-- join 한 테이블에서 인그리디언트로 그룹바이
-- 이후 토탈오더 썸
select i.INGREDIENT_TYPE, sum(f.TOTAL_ORDER) as total_order
from FIRST_HALF as f
join ICECREAM_INFO as i
on f.FLAVOR = i.FLAVOR
group by INGREDIENT_TYPE
order by 2 asc