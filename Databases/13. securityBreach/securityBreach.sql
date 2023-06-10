CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT first_name, second_name, attribute
FROM users
WHERE BINARY attribute LIKE  CONCAT('_%', CONCAT('\%',first_name, '\_',second_name,'\%'), '%');
	
END
