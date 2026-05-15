-- Last Updated: 5/15/2026, 11:13:55 PM
# Write your MySQL query statement below
select player_id,MIN(event_date) as first_login from Activity group by player_id;
