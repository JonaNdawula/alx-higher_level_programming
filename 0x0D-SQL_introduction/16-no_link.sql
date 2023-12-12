-- script 16
-- A script that lists all records of the 
-- table second_table of the database hbtn_0c_0
SELECT score, mname FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
