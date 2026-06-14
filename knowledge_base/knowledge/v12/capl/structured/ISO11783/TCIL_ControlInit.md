# TCIL_ControlInit

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ControlInit(); // form 1
```

## Description

This function can only be used in on preStart, to suppress the auto-start function of the IL.

If the device name is not specified, the node attributes with the device name must be defined (Exception: If NMT is not active, the device name is not needed).

## Return Values

0: Function has been executed successfully

## Example

```c
on preStart
{
 TCIL_ControlInit();
}
```

## Availability

| Since Version |
|---|
