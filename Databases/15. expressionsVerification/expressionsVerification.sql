CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id,a,b,operation,c 
	from expressions
	where (operation = '+' and a+b = c ) OR
	(operation = '-' and a-b = c ) OR
	(operation = '*' and a*b = c ) OR
	(operation = '/' and a/b = c )
	 order by id;
END
