CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	select WEEKDAY(mischief_date) as weekday, mischief_date, author, title from mischief
order by weekday, field(author, "Huey", "Dewey", "Louie"), mischief_date, title ;
END
