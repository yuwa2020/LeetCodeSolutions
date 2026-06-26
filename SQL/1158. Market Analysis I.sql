SELECT user_id AS buyer_id, join_date, COUNT(item_id) AS orders_in_2019
FROM Users
LEFT JOIN Orders ON buyer_id = user_id AND order_date BETWEEN "2019-01-01" AND "2019-12-31"
GROUP BY user_id, join_date