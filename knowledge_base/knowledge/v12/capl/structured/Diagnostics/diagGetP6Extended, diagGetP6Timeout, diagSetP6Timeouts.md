# diagGetP6Extended, diagGetP6Timeout, diagSetP6Timeouts

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetP6Extended(dword source);
```

## Description

Returns or sets the time P6 and P6ex (in milliseconds) from the given source.

If an ECU qualifier is given, the build-in communications channel for this target is accessed.

When a Diagnostics over IP target is active, the P2 timeouts cannot be used because a TCP/IP connection does not provide end of transmission and start of reception events. Therefore the P2 functionality cannot be implemented and the overall timeout P6 has been defined.

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 0 | Currently active value, i.e. the value originally set or last set from CAPL |
| 1 | Value stored at the selected interface in the description's document |
| 2 | Value configured in the configuration dialog for the description |
| other | reserved |

## Return Values

Error code

## Availability

| Since Version |
|---|
