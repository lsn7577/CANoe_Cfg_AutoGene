# J1939TestChkControl_Reset

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkControl_Reset( long checkId );
```

## Description

The status (stored values) of the check is initialized. The check does not have to be stopped for this function to work.

## Example

```c
long cycleCheck;
cycleCheck = J1939TestChkCreate_AbsCycleTimeViolation( 1, 2, 0xf123, 0.8, 1.2, "CycleCallback" );

J1939TestChkControl_Start( cycleCheck );
//...
J1939TestChkControl_Reset( cycleCheck );
```

## Availability

| Since Version |
|---|
