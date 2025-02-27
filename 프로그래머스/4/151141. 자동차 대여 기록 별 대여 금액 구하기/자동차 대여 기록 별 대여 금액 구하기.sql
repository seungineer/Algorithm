select HCP.history_id, round(HCP.FEE, 0) as FEE
from (
    select distinct HC.HISTORY_ID, case when days >= 7 and 30 > days and P.duration_type like '7일 이상' then HC.DAILY_FEE * days * (1 - P.DISCOUNT_RATE / 100)
                    when days >= 30 and 90 > days and P.duration_type like '30일 이상' then HC.DAILY_FEE * days * (1 - P.DISCOUNT_RATE / 100)
                    when days >= 90 and P.duration_type like '90일 이상' then HC.DAILY_FEE * days * (1 - P.DISCOUNT_RATE / 100)
                    when days < 7 then HC.DAILY_FEE * days
                    else null
            end as FEE,
            HC.days
    from (
        select H.HISTORY_ID, C.CAR_ID, datediff(H.END_DATE, H.START_DATE) + 1 as days, C.CAR_TYPE, C.DAILY_FEE
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY as H
        left join CAR_RENTAL_COMPANY_CAR as C
        on H.car_id = C.car_id) as HC
    left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as P
    on HC.car_type = P.car_type
    where HC.car_type like '트럭') as HCP
where not ISNULL(HCP.FEE)
order by 2 desc, 1 desc