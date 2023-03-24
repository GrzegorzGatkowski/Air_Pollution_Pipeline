select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

with all_values as (

    select
        pollution_quality as value_field,
        count(*) as n_records

    from `continual-block-378617`.`development`.`stg_air_pollution`
    group by pollution_quality

)

select *
from all_values
where value_field not in (
    'Very_Poor','Poor','Moderate','Fair','Good'
)



      
    ) dbt_internal_test