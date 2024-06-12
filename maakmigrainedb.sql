-- Create the migraine database
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'migraine')
    CREATE DATABASE migraine;
GO

-- Use the migraine database
USE migraine;
GO

-- Create the MigraineTriggers table
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'MigraineTriggers')
BEGIN
    CREATE TABLE MigraineTriggers (
        Id INT PRIMARY KEY,
        Name NVARCHAR(50) NOT NULL
    );

    -- Insert data into MigraineTriggers table
    INSERT INTO MigraineTriggers (Id, Name) VALUES
    (1, 'Stress'),
    (2, 'Gebrek aan slaap'),
    (3, 'Uitdroging'),
    (4, 'Hormonale veranderingen'),
    (5, 'Veranderingen in het weer'),
    (6, 'Voedingsmiddelen'),
    (7, 'Anders');
END;
GO

-- Create the Symptoms table
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Symptoms')
BEGIN
    CREATE TABLE Symptoms (
        Id INT PRIMARY KEY,
        Name NVARCHAR(50) NOT NULL
    );

    -- Insert data into Symptoms table
    INSERT INTO Symptoms (Id, Name) VALUES
    (1, 'Hoofdpijn'),
    (2, 'Duizeligheid'),
    (3, 'Gevoeligheid voor geuren'),
    (4, 'Gevoeligheid voor geluiden'),
    (5, 'Gevoeligheid voor kou');
END;
GO

-- Create the MigraineEntry table
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'MigraineEntry')
BEGIN
    CREATE TABLE MigraineEntry (
        Id INT PRIMARY KEY,
        Date DATETIME NOT NULL,
        PainScore INT NOT NULL,
        Medicine NVARCHAR(100),
        SymptomsId INT NOT NULL,
        TriggerId INT NOT NULL,
        FOREIGN KEY (SymptomsId) REFERENCES Symptoms(Id),
        FOREIGN KEY (TriggerId) REFERENCES MigraineTriggers(Id)
    );
END;
	GO
