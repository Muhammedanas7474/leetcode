# Write your MySQL query statement below
select unique_id,name from Employees e
left join EmployeeUNI as eni
on e.id =eni.id