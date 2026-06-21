-- Last Updated: 6/22/2026, 12:42:45 AM
# Write your MySQL query statement below
delete p1 from person p1
join person p2
on p1.email=p2.email and p1.id>p2.id