DROP TABLE IF EXISTS Products;

CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT, -- Automatically increment ProductID
    Name TEXT NOT NULL,                          -- Product name (e.g., Macbook Air)
    Category TEXT NOT NULL,                      -- Category (e.g., Electronics, Accessories)
    Color TEXT,                                  -- Optional field for product color
    Quantity INTEGER,                            -- Quantity in stock
    Price REAL NOT NULL                          -- Price of the product
);