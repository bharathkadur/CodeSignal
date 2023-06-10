CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT subscriber from full_year
	where newspaper like '%Daily%'
	UNION
	SELECT subscriber from half_year
	where newspaper like '%Daily%'
	order by subscriber;
END
