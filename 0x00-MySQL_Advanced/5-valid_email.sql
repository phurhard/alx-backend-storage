-- Creates a trigger which is useful for email validation
-- It reset the attribute valid_email

DELIMITER //

CREATE TRIGGER trigger_email_validation 
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        -- UPDATE users
        SET NEW.valid_email = CASE WHEN NEW.valid_email = 0 THEN 1 ELSE 0 END;
        -- WHERE id = NEW.id;
    END IF;
END //

DELIMITER ;
