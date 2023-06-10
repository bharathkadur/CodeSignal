CREATE PROCEDURE solution()
BEGIN
	select id, name,surname from Suspect 
	where height <= 170 
	and name LIKE 'B%' 
	and surname like 'Gre_n'
	order by id ASC;
END
