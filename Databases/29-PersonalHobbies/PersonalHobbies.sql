CREATE PROCEDURE solution()
BEGIN
	select name from people_hobbies
	where hobbies like "%reading%sports%";
END
