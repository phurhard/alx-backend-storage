-- Creates a script that will execute  trigger
-- the trigger decreases the quntity of an item after addinga new order

DELIMITER //

CREATE TRIGGER decreases_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number 
    WHERE name = NEW.item_name;
END //

DELIMITER ;
