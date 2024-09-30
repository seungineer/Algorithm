-- '경제 카테고리'
-- 오름차순 정렬
select B.BOOK_ID, A.AUTHOR_NAME, date_format(B.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book as B
left join author as A
on B.AUTHOR_ID = A.AUTHOR_ID
where category LIKE '경제'
order by 3 asc
