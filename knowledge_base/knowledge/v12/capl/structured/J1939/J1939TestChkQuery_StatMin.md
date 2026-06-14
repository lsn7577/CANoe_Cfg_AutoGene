# J1939TestChkQuery_StatMin

> Category: `J1939` | Type: `function`

## Syntax

```c
float J1939TestChkQuery_StatMin( long checkId );
```

## Description

This function returns the minimum value of the checked condition (cycle time, time distance or signal value).

## Example

```c
long cycleCheck;
cycleCheck = J1939TestChkCreate_AbsCycleTimeViolation( 1, 2, 0xf123, 0.8, 1.2, "CycleCallback" );

J1939TestChkControl_Start( cycleCheck );
//...
write( "Check Min. Cycle Time=%d", J1939TestChkQuery_StatMin(cycleCheck));
```

## Availability

| Since Version |
|---|
