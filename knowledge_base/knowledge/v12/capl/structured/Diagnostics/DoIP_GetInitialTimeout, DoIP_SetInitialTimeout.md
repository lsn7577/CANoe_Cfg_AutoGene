# DoIP_GetInitialTimeout, DoIP_SetInitialTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetInitialTimeout( dword toInitial_ms)
```

## Description

Sets or returns the initial timeout, started when a tester connects to the ECU (in milliseconds). A route activation request must be received in this interval, otherwise the TCP connection is closed.

If routing activation requests are switched off in the DoIP.INI via DisableRouteActivation, this timeout is not checked.

## Return Values

Form 1: —Form 2: Initial timeout

## Example

This value can also be configured in the DoIP.INI file.

```c
// Set T_TCP_Initial_Inactivity to 3s
DoIP_SetInitialTimeout( 3000);
```

## Availability

| Since Version |
|---|
