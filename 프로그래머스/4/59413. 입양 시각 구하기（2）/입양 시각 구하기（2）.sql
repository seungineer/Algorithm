set @HOUR := -1;
select @HOUR := @HOUR + 1 as HOUR,
    (select COUNT(*)
    from ANIMAL_OUTS as O
    where HOUR(O.DATETIME) = @HOUR) as COUNT
from ANIMAL_OUTS
where @HOUR < 23;