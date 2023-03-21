with airpollution as (
    select *,
    row_number() over(partition by City_index, dt) as rn
    from {{ source('staging','airpollution') }}
    order by City_index
)
select *
from airpollution
where rn = 1
limit 100