-- Last Updated: 6/22/2026, 12:42:54 AM
# Write your MySQL query statement below
select email from Person group by email having count(email)>1;