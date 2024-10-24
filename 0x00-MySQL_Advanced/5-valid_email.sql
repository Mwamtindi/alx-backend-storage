-- Create a trigger to reset valid_email when the email is updated

DELIMITER $$

CREATE TRIGGER reset_valid_email_on_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Reset valid_email to 0 only if the email has changed
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
