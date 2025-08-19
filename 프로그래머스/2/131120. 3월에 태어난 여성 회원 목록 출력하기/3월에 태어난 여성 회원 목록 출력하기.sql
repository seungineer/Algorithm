select member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d') as date_of_birth
from member_profile
where not isnull(tlno) and date_format(date_of_birth, '%m') like '03' and gender like 'W'
order by member_id