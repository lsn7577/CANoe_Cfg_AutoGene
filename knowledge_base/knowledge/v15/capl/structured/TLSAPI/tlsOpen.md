# tlsOpen

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
dword tlsOpen(dword socket);
```

## Description

Opens a TLS socket. An existing socket handle is used to create a new TLS connection.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |

## Example

```c
void OnTcpConnect( dword socket, long result)
{
  if (result == 0)
  {
    socket = tlsOpen(socket);
    tlsAuthenticateAsClient(socket, "");

    if ((tlsGetLastError(socket) != 0) &&
    (tlsGetLastError(socket) != 997))
    {
      // an error occurred
      return;
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP3 | 11.0 SP3 | 13.0 | — | — | 3.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
