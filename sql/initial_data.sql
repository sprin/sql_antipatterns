INSERT INTO Accounts (account_id, first_name, last_name) VALUES
  (1, 'brosef', 'bugdev'),
  (2, 'random', 'bugmagnet'),
  (3, 'bees', 'bugmenot');

INSERT INTO Products (product_id, product_name) VALUES
  (1, 'Open RoundFile'),
  (2, 'Visual TurboBuilder'),
  (3, 'ReConsider');

INSERT INTO BugStatus (status) VALUES
  ('NEW');

INSERT INTO Bugs (bug_id, reported_by, date_reported, summary, status) VALUES
  (1234, 2, TIMESTAMP '2004-10-19 10:23:54', 'crash when I save', 'NEW'),
  (2345, 2, TIMESTAMP '2004-10-20 10:23:54', 'increase performance', 'NEW'),
  (3456, 2, TIMESTAMP '2004-10-21 10:23:54', 'screen goes blank', 'NEW'),
  (5678, 2, TIMESTAMP '2004-10-22 10:23:54', 'unknown conflict between products', 'NEW');

INSERT INTO BugsProducts (bug_id, product_id) VALUES
  (1234, 1),
  (1234, 3),
  (3456, 2),
  (5678, 1),
  (5678, 3);

INSERT INTO Comments (comment_id, bug_id, author, comment_date, comment) VALUES
  (6789, 1234, 2, TIMESTAMP '2004-10-25 10:23:54', 'It crashes!'),
  (6790, 1234, 3, TIMESTAMP '2004-10-25 10:23:55', 'Fix it!'),
  (6850, 1234, 1, TIMESTAMP '2004-10-25 18:20:11', 'worksforme'),
  (9800, 2345, 2, TIMESTAMP '2004-10-26 10:23:54', 'Widgets are broken, maybe need to use Zappa 1.8 widgets?'),
  (9876, 2345, 1, TIMESTAMP '2004-10-26 12:23:54', 'Great idea... pffft');

