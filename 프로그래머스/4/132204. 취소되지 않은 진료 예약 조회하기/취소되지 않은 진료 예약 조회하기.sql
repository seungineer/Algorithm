select AD.APNT_NO, P.PT_NAME, AD.PT_NO, AD.MCDP_CD, AD.DR_NAME, AD.APNT_YMD
from (
    select A.APNT_NO, A.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD, A.APNT_CNCL_YMD, A.APNT_CNCL_YN
    from APPOINTMENT as A
    left join DOCTOR as D
    on A.MDDR_ID = D.DR_ID) as AD
left join PATIENT as P
on AD.PT_NO = P.PT_NO
where date_format(AD.APNT_YMD, '%Y-%m-%d') like '2022-04-13' and
    AD.APNT_CNCL_YN like 'N'
order by AD.APNT_YMD asc
    