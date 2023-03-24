with pollution as (
    select *,
    row_number() over(partition by City_index, dt) as rn
    from {{ source('source','airpollution') }}
    order by City_index
)
select City_index,
dt,
{{ get_pollution_quality('Sulfur_Dioxide_SO2', 'Nitrogen_Dioxide_NO2', 'PM10', 'PM2_5', 'Ozone_O3', 'Carbon_Monoxide_CO') }} as pollution_quality,
Sulfur_Dioxide_SO2,
Nitrogen_Dioxide_NO2,
PM10,
PM2_5,
Ozone_O3,
Carbon_Monoxide_CO,
NH3,
Nitric_oxide_NO
from pollution
where rn = 1

-- dbt build --m <model.sql> --var 'is_test_run: false'
{% if var('is_test_run', default=false) %}

  limit 300

{% endif %}
