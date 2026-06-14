# DoIP_SetProtocol

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetProtocol (dword protocolID);
```

## Description

Sets protocol version used in DoIP PDUs.

## Return Values

—

## Example

This value can also be configured globally on the diagnostics configuration dialog, DoIP Main Settings.

```c
// Use early draft version of the protocol
DoIP_SetProtocol(1);
```

## Availability

| Since Version |
|---|
