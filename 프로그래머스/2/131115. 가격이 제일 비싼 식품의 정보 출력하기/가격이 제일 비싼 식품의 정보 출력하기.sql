select *
from FOOD_PRODUCT
WHERE PRICE IN(
    select MAX(PRICE)
    from FOOD_PRODUCT)
