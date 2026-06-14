# DoIP_GetAliveCheckTimeout, DoIP_SetAliveCheckTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetAliveCheckTimeout(dword toAliveCheck_ms);
```

## Description

Sets or returns Alive Check Timeout (T_TCP_Alive_Check)) in milliseconds.

This function must be called in on preStart.

## Return Values

Form 1: —Form 2: The timeout parameter in milliseconds

## Example

This value can also be configured in the DoIP.INI file.

```c
// Set T_TCP_Alive_Check to 3s
DoIP_SetAliveCheckTimeout( 3000);
```

## Availability

| Since Version |
|---|
