# J1939TestChkControl_Start

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkControl_Start( long checkId );
```

## Description

Starts or continues checking the event condition. May work on a check stopped earlier, or on a check created in previously. Ignored for active checks.

## Example

```c
long cycleCheck;
cycleCheck = J1939TestChkCreate_AbsCycleTimeViolation( 1, 2, 0xf123, 0.8, 1.2, "CycleCallback" );
J1939TestChkControl_Start( cycleCheck );
```

## Availability

| Since Version |
|---|
