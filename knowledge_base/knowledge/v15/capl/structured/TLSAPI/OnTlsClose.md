# OnTlsClose

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
void OnTlsClose(dword socketHandle, int result);
```

## Description

If the CAPL program implements this callback it is called when the peer closes the tls connection while a receive call is pending.

## Parameters

| Name | Description |
|---|---|
| socket | The TLS socket handle. If the handle is valid (not equal to ~0), it corresponds to the socket that was used for tlsOpen. |
| result | The specific TLS result code. If the peer has closed the connection, the result is 4 (PeerClosed). |

## Return Values

—

## Example

```c
void OnTlsClose(dword socketHandle, int result)
{
  if(result == 4)
  {
    write("peer closed tls connection");
    TlsClose(socketHandle, 1);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 13.0 | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
