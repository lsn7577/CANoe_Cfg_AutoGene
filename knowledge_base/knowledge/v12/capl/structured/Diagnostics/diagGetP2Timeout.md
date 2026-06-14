# diagGetP2Timeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetP2Timeout (); // form 1: deprecated. Is equivalent to form 2 with source value 2.
```

## Description

Returns the time P2 in milliseconds, from the given source. If an ECU qualifier is given, the build-in communications channel for this target is accessed.

P2: Time between sending of the request and the start of the arrival of the first response.

The function will return different values for client (i.e. in a tester) and server (i.e. in an ECU simulation).

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 0 | Currently active value, i.e. the value originally set or last set from CAPL |
| 1 | Value stored at the selected interface in the description's document |
| 2 | Value configured in the configuration dialog for the description |
| other | reserved |

## Return Values

Error code or time in ms.

## Example

```c
diagSetTarget( "ECU1");
write( "Current P2 = %d", diagGetP2Timeout(0));
write( "Configured P2 = %d", diagGetP2Timeout(2));
```

## Availability

| Since Version |
|---|
