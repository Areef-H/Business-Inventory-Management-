-- Create the Products table
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY, -- Automatically increment ProductID
    Name TEXT NOT NULL,           -- Product name (e.g., Macbook Air)
    Category TEXT NOT NULL,       -- Category (e.g., Electronics, Accessories)
    Color TEXT,                   -- Optional field for product color
    Quantity INTEGER,             -- Quantity in stock
    Price REAL NOT NULL           -- Price of the product
);


CREATE TABLE Sales (
    SaleID INTEGER PRIMARY KEY ,
    ProductID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
);

