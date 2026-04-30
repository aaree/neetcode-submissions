-- Write your query below
select employee_id, case when employee_id%2=1 AND not starts_with(name, 'M') then salary else 0 end as bonus
from employees
order by 1