-- Write your query below
with test as (
    select distinct a.customer_id,a.customer_name, b.product_name
    from customers a inner join orders b
    on a.customer_id=b.customer_id
),
test2 as (
select customer_id,customer_name,sum(case when product_name='A' then 1 when product_name='B' then 1 else 0 end) as cntab, sum(case when product_name='C' then 1 else 0 end) as cntc
from test
group by customer_id,customer_name
)
select customer_id,customer_name
from test2
where cntab=2 and cntc=0
order by 2