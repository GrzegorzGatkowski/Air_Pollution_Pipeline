

with pollution as (
    select * from `continual-block-378617`.`development`.`fact_pollution`
)
    select 
        City,
        count(1) as days_count,
        pollution_quality
    from pollution
    group by 1, 3
    having City='Pszczyna'