CREATE PROCEDURE solution()
BEGIN
	select name from Products order by price * quantity desc, name limit 1;
END
