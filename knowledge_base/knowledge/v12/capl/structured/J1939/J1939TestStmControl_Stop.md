# J1939TestStmControl_Stop

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestStmControl_Stop( long stimulusId );
```

## Description

Turns off the sending of a Stimulus Parameter Group.

## Example

```c
long toggleStm;
pg MyPG myPG;

myPG.SA = 1;
myPG.DA = 2;

toggleStm = J1939TestStmCreate_Toggle( myPG, MyPg::SignalA, 100, 10, 20 );
J1939TestStmControl_Start( toggleStm );
//...
J1939TestStmControl_Stop(toggleStm);
```

## Availability

| Since Version |
|---|
