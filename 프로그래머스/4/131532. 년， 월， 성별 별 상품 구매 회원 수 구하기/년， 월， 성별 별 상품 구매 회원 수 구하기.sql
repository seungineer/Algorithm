select s.year, s.month, i.gender, count(distinct(i.user_id)) as users
from (
    select *, year(sales_date) as year, month(sales_date) as month
from online_sale
) as s
inner join
(select * from user_info where gender is not null) as i
on s.user_id = i.user_id
where i.gender is not null
group by s.year, s.month, i.gender
order by 1, 2, 3