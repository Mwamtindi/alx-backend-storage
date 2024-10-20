-- script that creates a function SafeDiv

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN CASE 
        WHEN b = 0 THEN 0
        ELSE a / b
    END;
END //

DELIMITER ;
