-- 2022년 5월 예약 환자 수를 진료과 코드 별로 조회
select MCDP_CD as '진료과코드', count(*) as '5월예약건수'
from APPOINTMENT
where APNT_YMD LIKE '2022-05-%'
group by MCDP_CD
order by 2 asc, 1 asc