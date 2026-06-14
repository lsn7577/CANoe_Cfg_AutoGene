# Iso11783IL_ControlInit

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_ControlInit();
```

## Description

This function can only be used in on preStart, to suppress the auto-start function of the IL.

If the device name is not specified, the node attributes with the device name must be defined (Exception: If NMT is not activate, the device name is not needed).

## Return Values

0 on success or error code

## Example

```c
on preStart
{
 Iso11783IL_ControlInit();
}
```

## Availability

| Since Version |
|---|
