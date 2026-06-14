# tlsClose

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsClose(dword socket, dword closeUnderlyingSocket);
```

## Description

Closes the given TLS connection. This sends a TLS alert message to the peer node. The underlaying socket will be closed automatically if the parameter closeUnderlyingSocket is set to a value greater 0.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| closeUnderlyingSocket | 0: do not close underlying socket. unequal 0: close the underlying socket. |

## Example

```c
void ClientStop()
{
  //
  // Close TLS socket and underlying socket
  //

  tlsClose(gTlsClientSocket, 1);
  gTlsClientSocket = 0;
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
