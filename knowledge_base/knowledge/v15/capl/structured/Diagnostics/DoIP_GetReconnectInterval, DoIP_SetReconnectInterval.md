# DoIP_GetReconnectInterval, DoIP_SetReconnectInterval

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
dword DoIP_GetReconnectInterval(); // form 1
void DoIP_SetReconnectInterval(dword reconnectInterval_ms, dword maxAttempts); // form 2
```

## Description

Get the distance between reconnect attempts by the tester, or configure the way the tester repeats reconnect attempts to the vehicle.

When the vehicle closes the connection the tester will wait for a time configured with DoIP_SetReconnectDelay before trying to connect to the vehicle again. It will then send up to maxAttempts TCP connection requests to the ECU, waiting reconnectInterval_ms between attempts.

## Parameters

| Name | Description |
|---|---|
| reconnectInterval_ms | After sending a TCP connection request the tester will wait this long for the vehicle to accept it. If it does not respond, the tester will send another request, unless the maximum number of attempts is reached. |
| maxAttempts | Maximum number of connection attempts the tester will perform. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | — | — | — | 2.1 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
