select distinct C.CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as H
left join CAR_RENTAL_COMPANY_CAR as C
on H.CAR_ID = C.CAR_ID
where C.CAR_TYPE like '세단' and MONTH(H.START_DATE) = 10
order by 1 desc