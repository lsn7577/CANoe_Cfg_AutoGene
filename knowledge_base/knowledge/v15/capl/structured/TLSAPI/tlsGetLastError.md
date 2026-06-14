# tlsGetLastError

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsGetLastError(dword socket);
```

## Description

Returns the TLS error code of the last operation that failed on a specified socket.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |

## Example

```c
void OnTcpListen( dword socket, long result)
{
  DWORD clientHandle;
  // Accept the connection
  clientHandle = TcpAccept( socket );

  tlsOpen(clientHandle);
  tlsAuthenticateAsServer(clientHandle, "Server1");

  if ((tlsGetLastError(clientHandle) != 0) &&
  (tlsGetLastError(clientHandle) != 997))
  {
    // an error occurred
    return;
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
