-- Write your PostgreSQL query statement below
select contest_id , round((count(*):: decimal /(select count(*) from Users ))*100,2)as percentage
from Users as a
 join Register as r
on a.user_id = r.user_id
group by contest_id 
order by round((count(*):: decimal /3)*100,2) desc,contest_id 
