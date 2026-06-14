# VTIL_ResetVTStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ResetVTStatus( ); // form 1
```

## Description

This function reverts changes made by SetVTStatus and turn back to the default behavior of the Virtual Terminal IL.

## Return Values

0: Function has been executed successfully

## Example

```c
if (VTIL_ResetVTStatus(VT) < 0)
{
  TestStepFail("Failed to reset VT Status message" );
}
```

## Availability

| Since Version |
|---|
