-- 대여중인 car_id를 서브쿼리로 만들어서
-- car_id가 해당 서브쿼리에 속하는 경우 "무조건" 대여중 아닌경우 대여가능
select car_id, case
when car_id in
(select car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date('2022-10-16') between start_date and end_date) then '대여중'
else '대여 가능'
end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by 1 desc