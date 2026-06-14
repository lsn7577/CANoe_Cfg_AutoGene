# J1939TestStmControl_Start

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestStmControl_Start( long stimulusId );
```

## Description

Starts or continues sending a Stimulus Parameter Group. May work on a Stimulus stopped earlier, or on a Stimulus created in previously. Ignored for active Stimuli.

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
