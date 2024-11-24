-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- That computes and store the average weighted score for a student
DROP procedure IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN


    -- Calculate the total weighted score and total weight for the given user_id
    SELECT SUM(score * weight), SUM(weight)
    INTO total_weighted_score, total_weight
    FROM corrections
    WHERE user_id = user_id;

    UPDATE users
   	SET average_score=(SELECT AVG(score) FROM corrections
			     WHERE corrections.user_id=user_id)
	WHERE id=user_id;
END;
|