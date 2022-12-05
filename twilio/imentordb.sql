CREATE TABLE Contacts (
    person_id int AUTO_INCREMENT,
    lname varchar(255),
    fname varchar(255),
    phone_number varchar(255),
    email varchar(255),
    PRIMARY KEY (person_id)
);

INSERT INTO Contacts (lname,fname, phone_number, email)
VALUES ("Athwal", "Harp", "+7322774364", "ha227@cornell.edu");

INSERT INTO Contacts (lname,fname, phone_number, email)
VALUES ("Suresh", "Anirudh", "+7186648010", "harpathwalwork@gmail.com");

INSERT INTO Contacts (lname,fname, phone_number, email)
VALUES ("Reed", "Jana", "+9174530567", "jreed@imentor.org");

-- mysql> SELECT * FROM Contacts;
-- +-----------+--------+---------+--------------+--------------------------+
-- | person_id | lname  | fname   | phone_number | email                    |
-- +-----------+--------+---------+--------------+--------------------------+
-- |         1 | Athwal | Harp    | +7322774364  | ha227@cornell.edu        |
-- |         2 | Suresh | Anirudh | +7186648010  | harpathwalwork@gmail.com |
-- |         3 | Reed   | Jana    | +9174530567  | jreed@imentor.org        |
-- +-----------+--------+---------+--------------+--------------------------+


CREATE TABLE Messages (
    message_id int AUTO_INCREMENT,
    from_phone_number varchar(255),
    message varchar(255),
    PRIMARY KEY (message_id)
);

INSERT INTO Messages ( from_phone_number, message) VALUES ("7322774364","Test Message");

