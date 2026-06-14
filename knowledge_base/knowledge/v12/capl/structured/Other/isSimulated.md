# isSimulated

> Category: `Other` | Type: `function`

## Syntax

```c
long isSimulated()
```

## Description

This function is used to get the information if CANoe is in simulated mode.

## Return Values

1: True, CANoe is in simulated mode.

## Example

This example checks if CANoe is in simulated mode. Then the test is not executed.

```c
// do not activate test when running in simulated mode
if (isSimulated())
{
Write("Test cannot run in simulated mode!");
}
```

## Availability

| Since Version |
|---|
