# J1939TestChkQuery_Count

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkQuery_Count( long checkId );
```

## Description

The function returns the number of measured values.

## Example

```c
long cycleCheck;
cycleCheck = J1939TestChkCreate_AbsCycleTimeViolation( 1, 2, 0xf123, 0.8, 1.2, "CycleCallback" );

J1939TestChkControl_Start( cycleCheck );
//...
write( "Number of values=%d", J1939TestChkQuery_Count(cycleCheck));
```

## Availability

| Since Version |
|---|
