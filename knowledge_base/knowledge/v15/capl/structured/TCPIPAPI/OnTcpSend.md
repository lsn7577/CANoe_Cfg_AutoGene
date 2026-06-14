# OnTcpSend

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpSend( dword socket, long result, char buffer[], dword size);
```

## Description

If the CAPL program implements this callback it is called when the data from the stack have been processed but not yet placed on the bus. The information is first displayed in the CANoe Trace Window when it has physically been sent.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle or socket object. |
| result | The result code of the asynchronous operation. If the operation completed successfully the value is 0. Otherwise the value is an error code. |
| buffer | The buffer provided with the send operation. |
| size | The number of bytes sent. |

## Return Values

—

## Example

```c
// ---------------------------------------------------
// When asynchronous TcpSend is complete...
// ---------------------------------------------------
void OnTcpSend( dword socket, long result, char buffer[], dword size)
{
  if (socket != ~0)
  {
    // sending data complete.
    If (result != 0)
    {
      writeLineEx(1, 3, “OnTcpSend error: %d”, result);
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 7.0 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
