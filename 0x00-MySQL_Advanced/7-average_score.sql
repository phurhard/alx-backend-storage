-- creates a stored procedure that computes and stores the average score for a student
-- an average can be decimal

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN users_id INT)
BEGIN
    DECLARE average_score DECIMAL(10, 2);
    SELECT AVG(score) INTO average_score FROM corrections WHERE user_id = users_id;
    UPDATE users SET average_score = average_score WHERE id = users_id;
    
END //

DELIMITER ;
