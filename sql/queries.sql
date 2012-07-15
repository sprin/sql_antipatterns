SELECT b.summary, c.comment, a.first_name
    FROM comments AS c
    JOIN accounts AS a ON a.account_id = c.author
    JOIN bugs AS b ON c.bug_id = b.bug_id
    WHERE a.first_name = 'brosef';

SELECT a.first_name, p.*
    FROM Products AS p
    JOIN Contacts AS c ON (p.product_id = c.product_id)
    JOIN Accounts AS a ON (c.account_id = a.account_id)
    WHERE a.first_name IN ('brosef', 'bees');

SELECT product_id, COUNT(*) AS accounts_per_products
    FROM CONTACTS
    GROUP BY product_id;

SELECT account_id, COUNT(*) AS products_per_account 
    FROM CONTACTS
    GROUP BY account_id;

SELECT c.product_id, c.contacts_per_product
    FROM (
        SELECT product_id, COUNT(*) AS contacts_per_product
        FROM Contacts
        GROUP BY product_id
    ) AS c
    ORDER BY c.contacts_per_product DESC LIMIT 1;
