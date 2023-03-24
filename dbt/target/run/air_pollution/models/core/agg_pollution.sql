
  
    

    create or replace table `continual-block-378617`.`development`.`agg_pollution`
    
    
    OPTIONS()
    as (
      

with pollution as (
    select * from `continual-block-378617`.`development`.`fact_pollution`
)
select 
    City,
    count(1) as hours_count,
    pollution_quality
from pollution
group by 1, 3
    );
  