# DoIP_GetGenericTimeout, DoIP_SetGenericTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetGenericTimeout( dword toGeneric_ms)
```

## Description

Sets or returns the generic timeout. The generic timeout specifies the maximum time of inactivity of the TCP connection before the connection is automatically closed.

## Return Values

Form 1: —Form 2: Timeout waiting for a diagnostic message positive or negative acknowledgment

## Example

This value can also be configured in the DoIP.INI file.

```c
// Set T_TCP_Generic_Inactivity to 30s
DoIP_SetGenericTimeout( 30000);
```

## Availability

| Since Version |
|---|
