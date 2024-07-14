DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score DECIMAL(5,2))
BEGIN
	-- Declare a local variable 'project_id' to store the project's ID
	DECLARE project_id INT;

	-- Check if the project alreafy exists
	SELECT id INTO project_id
	FROM projects
	WHERE name = project_name
	LIMIT 1;

	-- If the project does not exist, create it
	IF project_id IS NULL THEN
		INSERT INTO projects (name)
		VALUES (project_name);

		-- Get the new project's id
		SET project_id = LAST_INSERT_ID();
	END IF;

	-- Insert the correction for the student
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, project_id, score);
END //


DELIMITER ;
