# Iso11783IL_OPDeleteObjectPool

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPDeleteObjectPool(); // form 1
```

## Description

The function sends the Delete Object Pool message to the connected Virtual Terminal.

The simulated node neither clears the loaded Object Pool nor stops to send the Working Set Maintenance message to the Virtual Terminal.

For simultaneous clearing of the loaded Object Pool and stopping the Working Set Maintenance message, call the Iso11783IL_OPDeactivate() instead.

## Return Values

= 0: Function has been executed successfully

## Example

```c
long result;
result = Iso11783IL_OPDeleteObjectPool(Sprayer);
if (result < 0)
{
  TestStepFail("Failed to send the Delete Object Pool mesage");
}
```

## Availability

| Since Version |
|---|
