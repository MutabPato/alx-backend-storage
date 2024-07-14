-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create the user_averages table if it does not exist
CREATE TABLE IF NOT EXISTS user_averages(
	user_id INT PRIMARY KEY,
	average_score DECIMAL(5,2)
);

-- Delimiter for creating the procedure
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

	-- Insert or update the average score in the user_averages table
	INSERT INTO user_averages (user_id, average_score)
	VALUES (p_user_id, avg_score)
	ON DUPLICATE KEY UPDATE average_score = avg_score;
END //


DELIMITER ;
