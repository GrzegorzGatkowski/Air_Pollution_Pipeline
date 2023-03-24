select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select City_index
from `continual-block-378617`.`development`.`dim_pollution`
where City_index is null



      
    ) dbt_internal_test