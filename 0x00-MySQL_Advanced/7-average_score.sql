-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Delimeter for creating the procedure
DELIMITER //

-- Creating the procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
	-- Declare a local variable 'avg_score'
	DECLARE avg_score DECIMAL(5,2);

	-- Ccompute the average score for the given user
	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE user_id = p_user_id;

	-- Update the average score in the users table
	UPDATE users
	SET average_score = avg_score
	WHERE id = p_user_id;
END //


DELIMITER ;
