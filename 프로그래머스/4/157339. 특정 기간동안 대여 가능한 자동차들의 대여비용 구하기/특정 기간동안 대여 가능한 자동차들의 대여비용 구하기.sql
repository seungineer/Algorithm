-- 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중
-- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
-- 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차
SELECT CP.car_id, CP.car_type, FLOOR(CP.daily_fee * 30 * (1 - (CP.discount_rate / 100))) AS FEE
FROM (
    SELECT C.car_id, C.car_type, C.daily_fee, P.discount_rate
    FROM CAR_RENTAL_COMPANY_CAR AS C
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
    ON C.CAR_TYPE = P.CAR_TYPE
    WHERE C.CAR_TYPE IN ('세단', 'SUV') AND P.duration_type = '30일 이상'
) AS CP
WHERE CP.car_id NOT IN (
    SELECT car_id 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE (START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01')
)
AND FLOOR(CP.daily_fee * 30 * (1 - (CP.discount_rate / 100))) BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, CP.car_type ASC, CP.car_id DESC;
