CREATE DATABASE ecom_project;
USE ecom_project;

CREATE TABLE olist_data (
    Id INT,
    order_status STRING,
    order_products_value FLOAT,
    order_freight_value FLOAT,
    order_items_qty INT,
    customer_city STRING,
    customer_state STRING,
    customer_zip_code_prefix INT,
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    review_score INT,
    order_purchase_timestamp STRING,
    order_approved_at STRING,
    order_delivered_customer_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

LOAD DATA INPATH '/user/ecom-project/ecom-dataset.csv' INTO TABLE olist_data;