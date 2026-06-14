# J1939TestChkControl_Stop

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkControl_Stop( long checkId );
```

## Description

Turns off the checking of the event condition.

## Example

```c
long cycleCheck;
cycleCheck = J1939TestChkCreate_AbslCycleTimeViolation( 1, 2, 0xf123, 0.8, 1.2, "CycleCallback" );

J1939TestChkControl_Start( cycleCheck );
//...
J1939TestChkControl_Stop( cycleCheck );
```

## Availability

| Since Version |
|---|
