select *
from (
    select C.car_id,C.CAR_TYPE, FLOOR(C.DAILY_FEE * 30 * (1 - (P.DISCOUNT_RATE / 100))) as FEE
    from CAR_RENTAL_COMPANY_CAR as C
    join (select * from CAR_RENTAL_COMPANY_DISCOUNT_PLAN where DURATION_TYPE LIKE '30일 이상' and CAR_TYPE IN ('세단','SUV')) as P
    on C.CAR_TYPE = P.CAR_TYPE
    where  C.DAILY_FEE * 30 * (1 - (P.DISCOUNT_RATE / 100)) >= 500000
    and C.DAILY_FEE * 30 * (1 - (P.DISCOUNT_RATE / 100)) < 2000000
) as CP
where CP.car_id NOT IN (
select H.car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as H
where H.START_DATE <= DATE('2022-11-30') and
H.END_DATE >= DATE('2022-11-01'))
order by 3 DESC, 2 ASC, 1 DESC