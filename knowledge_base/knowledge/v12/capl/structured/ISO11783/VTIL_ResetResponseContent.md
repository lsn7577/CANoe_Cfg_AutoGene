# VTIL_ResetResponseContent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ResetResponseContent(dbNode workingSetMaster, byte vtFunction); // form 1
```

## Description

The function resets the response modification of VTIL_SetResponseContent. Afterwards the default response is sent by the VT IL.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_ResetResponseContent(VT, Sprayer, 168);
if (result < 0)
{
  TestStepFail("Failed to reset fault injection");
}
```

## Availability

| Since Version |
|---|
