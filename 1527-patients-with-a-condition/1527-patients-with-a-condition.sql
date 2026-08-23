SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%'     -- starts with DIAB1
   OR conditions LIKE '% DIAB1%';  -- space before DIAB1
