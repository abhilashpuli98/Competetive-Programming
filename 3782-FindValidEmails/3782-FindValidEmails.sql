-- Last Updated: 5/15/2026, 11:09:56 PM
# Write your MySQL query statement below
select user_id,email from users
where email REGEXP '^[A-Za-z0-9_]+@[A-Za-z]+\\.com$'
order by user_id