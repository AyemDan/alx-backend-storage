-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- That computes and store the average weighted score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare variables to hold the total weighted score and total weight
    DECLARE total_weighted_score DECIMAL(10,2) DEFAULT 0;
    DECLARE total_weight DECIMAL(10,2) DEFAULT 0;
    DECLARE avg_weighted_score DECIMAL(10,2);

    -- Calculate the total weighted score and total weight for the given user_id
    SELECT SUM(score * weight), SUM(weight)
    INTO total_weighted_score, total_weight
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average weighted score if the total weight is greater than 0
    IF total_weight > 0 THEN
        SET avg_weighted_score = total_weighted_score / total_weight;
    ELSE
        SET avg_weighted_score = NULL;  -- Return NULL if no scores are found for the user
    END IF;

    -- Optionally, you can store the result in another table, or return it. 
    -- Here, we assume that you want to update a user record with this value. 

    -- Example: Update the user's average weighted score in the users table
    UPDATE users
    SET average_weighted_score = avg_weighted_score
    WHERE id = user_id;
    
END $$

DELIMITER ;
