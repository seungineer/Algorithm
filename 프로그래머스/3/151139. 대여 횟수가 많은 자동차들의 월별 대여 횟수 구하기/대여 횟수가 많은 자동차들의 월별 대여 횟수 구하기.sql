select month(start_date) as month, car_id, count(*) as records
from car_rental_company_rental_history as o
where o.car_id in (
    select car_id
    from car_rental_company_rental_history
    where month(start_date) >= 8 and month(start_date) <= 10 and year(start_date) = 2022
    group by car_id
    having count(*) >= 5
) and month(start_date) >= 8 and month(start_date) <= 10 and year(start_date) = 2022
group by car_id, month(start_date)
order by month asc, car_id desc