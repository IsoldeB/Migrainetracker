-- Truncate existing data to start fresh
TRUNCATE TABLE MigraineTriggers;
TRUNCATE TABLE Symptoms;
TRUNCATE TABLE MigraineEntry;

-- Declare variables
DECLARE @startDate DATETIME = '2023-01-01';
DECLARE @endDate DATETIME = '2023-12-31';
DECLARE @numEntries INT = 100; -- Number of random entries to generate

-- Insert random MigraineTriggers if they do not already exist
INSERT INTO MigraineTriggers (Id, Name)
SELECT Id, Name
FROM (
    VALUES 
    (1, 'Stress'),
    (2, 'Gebrek aan slaap'),
    (3, 'Uitdroging'),
    (4, 'Hormonale veranderingen'),
    (5, 'Veranderingen in het weer'),
    (6, 'Voedingsmiddelen'),
    (7, 'Anders')
) AS t(Id, Name)
WHERE NOT EXISTS (
    SELECT 1 FROM MigraineTriggers WHERE Id = t.Id
);

-- Insert random Symptoms if they do not already exist
INSERT INTO Symptoms (Id, Name)
SELECT Id, Name
FROM (
    VALUES 
    (1, 'Hoofdpijn'),
    (2, 'Duizeligheid'),
    (3, 'Gevoeligheid voor geuren'),
    (4, 'Gevoeligheid voor geluiden'),
    (5, 'Gevoeligheid voor kou')
) AS t(Id, Name)
WHERE NOT EXISTS (
    SELECT 1 FROM Symptoms WHERE Id = t.Id
);

-- Insert random MigraineEntry if they do not already exist
INSERT INTO MigraineEntry (Id, Date, PainScore, Medicine, SymptomsId, TriggerId)
SELECT 
    Id,
    Date,
    PainScore,
    Medicine,
    SymptomsId,
    TriggerId
FROM (
    SELECT 
        ROW_NUMBER() OVER(ORDER BY (SELECT NULL)),
        DATEADD(DAY, ROUND(RAND(CHECKSUM(NEWID())) * DATEDIFF(DAY, @startDate, @endDate), 0), @startDate),
        ROUND(RAND() * 10, 0),
        'Medicine ' + CAST(ROW_NUMBER() OVER(ORDER BY (SELECT NULL)) AS NVARCHAR(10)),
        ROUND(RAND() * @numEntries, 0) + 1,
        ROUND(RAND() * @numEntries, 0) + 1
    FROM sys.objects
) AS t(Id, Date, PainScore, Medicine, SymptomsId, TriggerId)
WHERE NOT EXISTS (
    SELECT 1 FROM MigraineEntry WHERE Id = t.Id
);
