ALTER TABLE Fine_Installments
ADD COLUMN IssuerReceiverID INT,
ADD FOREIGN KEY (IssuerReceiverID) REFERENCES Book_Issuer_Receiver(IssuerReceiverID);



INSERT INTO Fine_Installments (FineID, InstallmentNumber, InstallmentAmount, IssuerReceiverID) VALUES
(5, 2, 50.00, 1),
(10, 3, 75.00, 2),
(15, 4, 60.00, 1),
(7, 5, 80.00, 2),
(12, 6, 55.00, 1),
(3, 7, 70.00, 2),
(18, 8, 65.00, 1),
(2, 9, 45.00, 2),
(9, 10, 85.00, 1),
(11, 2, 40.00, 2),
(6, 3, 65.00, 1),
(19, 4, 55.00, 2),
(8, 5, 70.00, 1),
(17, 6, 50.00, 2),
(4, 7, 80.00, 1),
(13, 8, 60.00, 2),
(20, 9, 45.00, 1),
(1, 10, 75.00, 2),
(14, 2, 55.00, 1),
(16, 3, 70.00, 2);
