# J1939TestChkControl_Destroy

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkControl_Destroy_Destroy( long checkId );
```

## Description

The check is destroyed and cannot be accessed anymore. Its resources are freed and may be reused.

## Example

```c
long cycleCheck;
cycleCheck = J1939TestChkCreate_AbsCycleTimeViolation( 1, 2, 0xf123, 0.8, 1.2, "CycleCallback" );

J1939TestChkControl_Start( cycleCheck );
//...
J1939TestChkControl_Destroy_Destroy( cycleCheck );
```

## Availability

| Since Version |
|---|
