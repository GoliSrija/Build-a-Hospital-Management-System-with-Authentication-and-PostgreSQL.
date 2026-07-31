```sql
-- Insert users
INSERT INTO users (email, password, name)
VALUES 
('john.doe@example.com', 'password123', 'John Doe'),
('jane.doe@example.com', 'password123', 'Jane Doe');

-- Insert posts
INSERT INTO posts (user_id, title, content)
VALUES 
(1, 'Hello world', 'This is my first post'),
(1, 'My second post', 'This is my second post'),
(2, 'Welcome', 'Welcome to our website');

-- Insert comments
INSERT INTO comments (post_id, user_id, content)
VALUES 
(1, 1, 'Great post!'),
(1, 2, 'Nice post!'),
(2, 1, 'Hello!'),
(3, 1, 'Welcome!');
```