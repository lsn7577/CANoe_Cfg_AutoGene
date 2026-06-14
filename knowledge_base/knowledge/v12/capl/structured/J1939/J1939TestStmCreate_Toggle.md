# J1939TestStmCreate_Toggle

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestStmCreate_Toggle( pg aPg, dbSignal aSignal, dword cycleTime, float value1, float value2 );
```

## Description

Creates a Toggle Stimulus. The Stimulus toggles the signal between the two given values.

## Example

```c
long toggleStm;
pg MyPG myPG;

myPG.SA = 1;
myPG.DA = 2;

toggleStm = J1939TestStmCreate_Toggle( myPG, MyPg::SignalA, 100, 10, 20 );
J1939TestStmControl_Start(toggleStm);
```

## Availability

| Since Version |
|---|
