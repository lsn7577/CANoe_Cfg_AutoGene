# DoIP_SetPowerModeInformation

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetPowerModeInformation(long powerMode);
```

## Description

Sets the value returned automatically for a Power Mode Information Request.

## Return Values

—

## Example

```c
// The ECU simulation will return “ready” if the power mode is requested
DoIP_SetPowerModeInformation( 1);
```

## Availability

| Since Version |
|---|
