set @hour := -1;
select @hour := @hour + 1 as HOUR,
    (select COUNT(*)
    from ANIMAL_OUTS as O
    where HOUR(O.DATETIME) = @hour) as COUNT
from ANIMAL_OUTS
where @hour < 23;