# DoIP_GetReconnectInterval, DoIP_SetReconnectInterval

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
dword DoIP_GetReconnectInterval();
```

## Description

Get the distance between reconnect attempts by the tester, or configure the way the tester repeats reconnect attempts to the vehicle.

When the vehicle closes the connection the tester will wait for a time configured with DoIP_SetReconnectDelay before trying to connect to the vehicle again. It will then send up to maxAttempts TCP connection requests to the ECU, waiting reconnectInterval_ms between attempts.

## Return Values

Form 1: dword reconnectInterval_ms
Form 2: void

## Example

This value can also be configured in the DoIP.INI file.

```c
void Configure_DoIP()
{
  //...
  // Configure up to 15 attempts every 200 ms ...
  DoIP_SetReconnectInterval( 200, 15);

  // ... starting 500 ms after the vehicle closes the connection
  DoIP_SetReconnectDelay( 500);

  // Note that it may take over 500 ms + 15 * 200 ms = 3500 ms for the tester to
  // detect that the vehicle is no longer present!
  // Wait functions must take this into account.
}
```

## Availability

| Since Version |
|---|
