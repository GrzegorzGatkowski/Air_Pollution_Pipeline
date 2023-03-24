

  create or replace view `continual-block-378617`.`development`.`stg_cities`
  OPTIONS()
  as with cities as (
    select *,
    row_number() over(partition by City_index) as rn
    from `continual-block-378617`.`raw`.`cities`
    order by City_index
)
select City_index,
City,
Latitude,
Longitude
from cities
where rn = 1;

