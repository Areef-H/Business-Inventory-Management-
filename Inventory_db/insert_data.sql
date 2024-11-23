
INSERT INTO Products (Name, Category, Color, Quantity, Price)
VALUES 
    -- Macbook Products
    ('Macbook Air', 'Electronics', 'Space Gray', 35, 999.00),
    ('Macbook Pro', 'Electronics', 'Midnight', 30, 1299.00),

    -- iMac
    ('iMac 24-inch', 'Electronics', 'Blue', 25, 1299.00),
    ('Mac Mini', 'Electronics', 'Space Gray', 25, 699.00),

    -- iPhone Products
    ('iPhone 13', 'Electronics', 'Space Gray', 25, 599.00),
    ('iPhone 14', 'Electronics', 'Space Gray', 25, 799.00),
    ('iPhone 15', 'Electronics', 'Space Gray', 25, 899.00),
    ('iPhone 16', 'Electronics', 'Space Gray', 25, 999.00),

    -- Cases
    ('Magsafe Case - iPhone 14', 'Accessories', 'Mahogany', 25, 49.00),
    ('Magsafe Case - iPhone 14', 'Accessories', 'Space Gray', 25, 49.00),
    ('Magsafe Case - iPhone 15', 'Accessories', 'Space Gray', 25, 49.00),

    -- Mechanical Parts
    ('Apple Mac Pro Wheels Kit', 'Mechanical Parts', NULL, 10, 699.00),

    -- Software
    ('iCloud+ 50GB', 'Software', NULL, NULL, 0.99),
    ('iCloud+ 200GB', 'Software', NULL, NULL, 2.99),
    ('iCloud+ 2TB', 'Software', NULL, NULL, 9.99);


INSERT INTO Sales (ProductID, Quantity)
VALUES 
    (1, 3),  -- 3 units of "Macbook Air"
    (2, 2),  -- 2 units of "Macbook Pro"
    (5, 5),  -- 5 units of "iPhone 13"
    (10, 1), -- 1 unit of "Magsafe Case - iPhone 14"
    (13, 1); -- 1 subscription of "iCloud+ 2TB"



