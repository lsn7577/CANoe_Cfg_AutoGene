# Iso11783IL_PDDSetValueRaw, Iso11783IL_PDDSetValuePhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetValueRaw(dword ddi, dword elementNumber, long value); // form 1
```

## Description

Sets the value of a data entity (process variable) without sending any command.

## Example

```c
SetActualAppRateUsingRawValue()
{
  // section 1: elementNumber = 3
  Iso11783IL_PDDSetValuePhysical(Sprayer, 37, 3, 13.360);
  // section 2: elementNumber = 4
  Iso11783IL_PDDSetValuePhysical(Sprayer, 37, 4, 13.950);
}
```

## Availability

| Since Version |
|---|
