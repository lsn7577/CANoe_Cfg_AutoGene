# J1939TestChkQuery_Last

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkQuery_Last( long checkId );
```

## Description

The function returns the last measured value.

## Example

```c
long cycleCheck;
cycleCheck = J1939TestChkCreate_AbsCycleTimeViolation( 1, 2, 0xf123, 0.8, 1.2, "CycleCallback" );

J1939TestChkControl_Start( cycleCheck );
//...
write( "Last measured value=%d", J1939TestChkQuery_Last(cycleCheck));
```

## Availability

| Since Version |
|---|
