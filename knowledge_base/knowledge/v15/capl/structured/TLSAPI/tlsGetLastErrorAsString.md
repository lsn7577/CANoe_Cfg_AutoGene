# tlsGetLastErrorAsString

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsGetLastErrorAsString(dword socket, char buffer[], dword bufferLength );
```

## Description

Retrieves the error message of the last operation that failed on a specified socket.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| buffer | The buffer used to store the error message. |
| bufferLength | The size of the text buffer. |

## Example

```c
tlsOpen(clientHandle);
tlsAuthenticateAsServer(clientHandle, "Server1");

if ((tlsGetLastError(clientHandle) != 0) &&
   (tlsGetLastError(clientHandle) != 997))
{
  // an error occurred
  tlsGetLastErrorAsString(clientHandle, errorText, elcount(errorText));
  write( "tlsAuthenticateAsServer failed, %s (Result %d)", errorText,tlsGetLastError(clientHandle) );
  return;
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
