# Advanced mySQL
* treating topics like procedure, functions, indexing and the likes

## Stored Procedure

A stored procedure is a set of SQL statements that perform a specific task or a series of tasks. it can accept input parameters and return output parameters.

- synthax for creating a procedure

```sql
DELIMITER // the delimiter is changed from the default delimiter(;) to //
CREATE PROCEDURE procedure_name (parameters datatype1, parameters datatype2, ...)
BEGIN
    -- SQL Statements
END //
DELIMITER ; // the delimeter is changed back to ;
```
A stored procedure to get the students in a class

```sql
DELIMITER //
CREATE PROCEDURE studentsInAClass(IN class_id int)
BEGIN
    SELECT * FROM students WHERE class_id = class_id;
END //

DELIMITER ;
```

to call this procedure we use
```sql
CALL studentsInAClass(1);
```

## Functions

A function is similar to a stored procedure except it returns a value, it can be used anywhere an expression is required.

- synthax for creating a function

```sql
DELIMITER //
CREATE FUNCTION function_name (params datatype, ...)
RETURNS datatype
BEGIN
    -- SQL statements
    RETURN something;
END //

DELIMETER ;
```
A simple function that calculates the total score for a student

```sql
DELIMITER //
CREATE FUNCTION total_score(IN class_id int) RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE total_score DECIMAL(10, 2)
    SELECT SUM(score) INTO total_score FROM students WHERE class_id = class_id
    RETURN total_score;
END //
DELIMITER ;
```
to use the function in a query 
```sql
SELECT total_score(1) AS total_score;
```

## Views

Views are a way to represent complex SQL query functions as a separate table so that it eases querying the tables.

- synthax:

```sql
CREATE VIEW view_name AS SELECT column1, column2, ... FROM tables WHERE condition;
```

To create a view of teachers and the class they teach

```sql
CREATE VIEW teacherSubject AS SELECT s.class_name, t.full_name, s.subject_name FROM teachers t
JOIN subjects s ON t.subject_name = s.subject_name;
```
Once a view is created it can be queried like a regular table.
```sql
SELECT * FROM teacherSubject;
```

views can be updated by using the 

```CREATE OR REPLACE VIEW```

if the view is not available it'll be created otherwise it'll update it.

to drop a view

```DROP VIEW IF EXISTS teacherSubject;```

## Triggers

Triggers are set of instructions that are automatically executed in response to certain events on a partucular table or view

- synthax:

    ```sql
        CREATE TRIGGER trigger_name BEFORE|AFTER INSERT|UPDATE|DELETE ON     table_name
        FOR EACH ROW
        BEGIN  
        -- SQL statements
        END;
    ```

Triggers are implemented in ORM's declaration of models if there are foreign key relationship between them like in django when model is defined
```
    class MyModel(model.Model):
        name = models.ForeignKey('User', ON_DELETE=NULL)
```

The ```ON_DELETE=NULL``` is a trigger set such that once that relationship is deleted all the rest of the instance is set to NULL
