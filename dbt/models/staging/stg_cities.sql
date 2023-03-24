with cities as (
    select *,
    row_number() over(partition by City_index) as rn
    from {{ source('source','cities') }}
    order by City_index
)
select City_index,
City,
Latitude,
Longitude
from cities
where rn = 1
