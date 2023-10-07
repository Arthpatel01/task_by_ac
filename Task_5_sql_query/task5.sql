SELECT
    DateTime
FROM (
    SELECT
        DateTime,
        AVG(Price) AS AvgPrice
    FROM
        your_table_name
    GROUP BY
        DateTime
    ORDER BY
        AvgPrice
    LIMIT 2
) AS Subquery
ORDER BY
    AvgPrice
LIMIT 1;
