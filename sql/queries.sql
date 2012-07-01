SELECT b.summary, c.comment, a.first_name
    FROM comments AS c
    JOIN accounts AS a ON a.account_id = c.author
    JOIN bugs AS b ON c.bug_id = b.bug_id
    WHERE a.first_name = 'brosef';
