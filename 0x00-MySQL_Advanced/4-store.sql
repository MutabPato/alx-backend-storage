-- Delimeter for creating the trigger
DELIMITER //

-- Drop the trigger if it exists
DROP TRIGGER IF EXISTS decrease;

-- Trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER decrease
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;
//

-- Reset the delimeter to the default
DELIMITER ;
