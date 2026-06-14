# TCIL_ResetResponseContent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ResetResponseContent(dbNode client, dword command, dword subcommand); // form 1
```

## Description

The function resets the modification of TCIL_SetResponseContent. The TC IL returns to the default response behaviour.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = TCIL_ResetResponseContent(TC, Sprayer, 168);
if (result < 0)
{
  TestStepFail("Failed to reset fault injection");
}
```

## Availability

| Since Version |
|---|
