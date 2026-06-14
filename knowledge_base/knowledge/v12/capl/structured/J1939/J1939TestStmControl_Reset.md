# J1939TestStmControl_Reset

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestStmControl_Reset( long stimulusId );
```

## Description

Resets the value of the Stimulus Parameter Group. The Stimulus starts from the beginning.

## Example

```c
long toggleStm;
pg MyPG myPG;

myPG.SA = 1;
myPG.DA = 2;

toggleStm = J1939TestStmCreate_Toggle( myPG, MyPg::SignalA, 100, 10, 20 );

J1939TestStmControl_Start( toggleStm );
//...
J1939TestStmControl_Reset( toggleStm );
```

## Availability

| Since Version |
|---|
