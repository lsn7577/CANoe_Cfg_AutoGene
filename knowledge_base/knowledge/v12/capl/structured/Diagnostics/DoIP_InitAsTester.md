# DoIP_InitAsTester

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_InitAsTester();
```

## Description

Per default the DoIP.DLL will operate as ECU simulation. In order to use this DLL as tester, e.g. in a test module, the operation mode has to be changed by calling this function in on preStart. It is NOT necessary to call this function when the built-in diagnostics channel is used, i.e. if the DoIP.DLL is not configured in the tester.

## Return Values

—

## Example

```c
on preStart
{
  // Make sure the DoIP.DLL does not act as vehicle
  DoIP_InitAsTester();
}
```

## Availability

| Since Version |
|---|
