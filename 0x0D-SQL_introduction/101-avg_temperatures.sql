-- select the fields
 SELECT city, AVG(value) AS avg_temp
FROM temperatures
-- group them by the city
GROUP BY city
-- order the results by the average temperature in descending order
ORDER BY avg_temp
DESC;
