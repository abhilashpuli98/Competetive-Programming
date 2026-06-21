-- Last Updated: 6/21/2026, 7:05:49 PM
SELECT customer_number
FROM Orders 
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1;