select count(*) as FISH_COUNT
from FISH_INFO
where FISH_TYPE IN (
    select FISH_TYPE
    from FISH_NAME_INFO
    where FISH_NAME like 'BASS' or FISH_NAME like 'SNAPPER'
)
