-- Last Updated: 6/22/2026, 12:42:53 AM
# Write your MySQL query statement below
select name as Customers  from Customers where id not in(select customerId from Orders);
