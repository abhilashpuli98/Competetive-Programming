-- Last Updated: 6/21/2026, 7:05:45 PM
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;