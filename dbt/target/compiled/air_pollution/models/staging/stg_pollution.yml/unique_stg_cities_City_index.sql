
    
    

with dbt_test__target as (

  select City_index as unique_field
  from `continual-block-378617`.`development`.`stg_cities`
  where City_index is not null

)

select
    unique_field,
    count(*) as n_records

from dbt_test__target
group by unique_field
having count(*) > 1


