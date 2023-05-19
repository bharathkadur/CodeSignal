CREATE PROCEDURE solution()
    SELECT email
    FROM users
    WHERE role Not in("admin", "premium")

    ORDER BY email;
