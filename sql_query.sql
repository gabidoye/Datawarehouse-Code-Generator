DROP TABLE IF EXISTS dwh.stg.dim_invoice;
CREATE TABLE dwh.stg.dim_invoice (
  invoiceid int,
  linenumber int,
  invoicedate date,
  suppliername varchar(50),
  description nvarchar(255),
  PRIMARY KEY (invoiceid)
);

DROP TABLE IF EXISTS dwh.stg.dim_po3;
CREATE TABLE dwh.stg.dim_po3 (
  poid int,
  poline int,
  podate date,
  description nvarchar(255),
  PRIMARY KEY (poid)
);

DROP TABLE IF EXISTS dwh.stg.dim_supplier;
CREATE TABLE dwh.stg.dim_supplier (
  supplierid varchar(20),
  companyname nvarchar(50),
  location nvarchar(50),
  PRIMARY KEY (supplierid)
);

DROP TABLE IF EXISTS dwh.stg.fact_supplier_transaction;
CREATE TABLE dwh.stg.fact_supplier_transaction (
  sk_trans INT IDENTITY (1, 1) PRIMARY KEY,
  invoiceid INT,
  poid INT,
  supplierid INT,
  amount float,
  quantity float,
  discount float,
  CONSTRAINT FK_dim_invoice FOREIGN KEY (invoiceid) REFERENCES dwh.stg.dim_invoice(invoiceid),
  CONSTRAINT FK_dim_po3 FOREIGN KEY (poid) REFERENCES dwh.stg.dim_po3(poid),
  CONSTRAINT FK_dim_supplier FOREIGN KEY (supplierid) REFERENCES dwh.stg.dim_supplier(supplierid)
);