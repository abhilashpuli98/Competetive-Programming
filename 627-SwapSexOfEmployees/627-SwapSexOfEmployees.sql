-- Last Updated: 5/15/2026, 11:15:34 PM
# Write your MySQL query statement below
update salary
set sex =  case when sex="f" then "m"
when sex = "m" then "f"
end;