-- List records with score >= 10, showing score and name ordered by score descending

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
