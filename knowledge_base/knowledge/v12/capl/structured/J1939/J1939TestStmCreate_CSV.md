# J1939TestStmCreate_CSV

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestStmCreate_CSV( pg aPg, dbSignal aSignal, dword cycleTime, char csvFile[] );
```

## Description

Creates a CSV Stimulus. The values for the Stimulus are loaded from a CSV file.

## Example

```c
long csvStm;
pg MyPG myPG;

myPG.SA = 1;
myPG.DA = 2;

csvStm = J1939TestStmCreate_CSV( myPG, MyPg::SignalA, 100, "Values.csv" );
J1939TestStmControl_Start(csvStm);
```

## Availability

| Since Version |
|---|
