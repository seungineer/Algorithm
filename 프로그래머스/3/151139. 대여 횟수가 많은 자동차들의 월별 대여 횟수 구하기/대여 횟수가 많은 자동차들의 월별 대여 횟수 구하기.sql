with filtered as (
select *, month(start_date) as month
    from car_rental_company_rental_history
    where year(start_date) = 2022 and month(start_date) between 8 and 10
)

select month, car_id, count(*) as records
from filtered
where car_id in (
    select car_id
    from (
        select month, car_id, count(*) as cnts
        from filtered   
        group by car_id, month
    ) as tmp
    group by tmp.car_id
    having sum(cnts) >= 5
)
group by car_id, month
order by 1 asc, 2 desc

