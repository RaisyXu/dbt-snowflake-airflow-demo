select 
    item_discount_amount
from
    {{ ref('fct_orders') }}
where
   item_discount_amount > 0