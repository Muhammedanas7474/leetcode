-- Write your PostgreSQL query statement below
select name from (
    select m.id,m.name
from Employee as e
join Employee as m
on e.managerId=m.id
group by m.id ,m.name
having count(*) >= 5
) 




