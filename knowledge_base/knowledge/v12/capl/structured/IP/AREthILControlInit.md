# AREthILControlInit

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthILControlInit();
```

## Description

Initialization of AUTOSAR Eth IL.

Prevents the AUTOSAR Eth IL from starting automatically. If this function is used, the AUTOSAR Eth IL must then be started with the AREthILControlStart function.

This function may only be used in on preStart.

## Return Values

0: The function was successfully executed

## Example

```c
on preStart
{
  // prevent auto start
  AREthILControlInit();
}
```

## Availability

| Since Version |
|---|
