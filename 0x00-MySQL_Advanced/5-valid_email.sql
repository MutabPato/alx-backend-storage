-- Delimeter for creating the trigger
DELIMITER //

-- Drop the trigger if it exists
DROP TRIGGER IF EXISTS new_email;

-- creates a trigger that resets the attribute valid_email only when the email has been changed
CREATE TRIGGER new_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;
//

-- Reset the delimeter to the default
DELIMITER ;
