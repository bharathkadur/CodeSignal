CREATE PROCEDURE solution()
BEGIN
	select project_name, team_lead, income from Projects ORDER BY internal_id ASC;
END
