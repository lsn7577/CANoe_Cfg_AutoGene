# OnTlsHandshakeComplete

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
void OnTlsHandshakeComplete(dword socket, long result);
```

## Description

If the CAPL program implements this callback it is called when a TLS handshake is completed.

## Parameters

| Name | Description |
|---|---|
| socket | The TLS socket handle. If the handle is valid (not equal to ~0), it corresponds to the socket that was used for tlsOpen. |
| result | The specific result code of the operation. If the operation completed successfully the value is zero. Otherwise the value is an error code. |

## Return Values

—

## Example

```c
void OnTlsHandshakeComplete(dword socket, long result)
{
  LONG retVal;
  if (result == 0)
  {
    gConnectionSecured = 1;

    //
    // Send first message
    //
    retVal = TcpSend( socket, "The TLS connection is up", 25 );
    
if (retVal != 0)
    {
      // an error occurred
      return;
    }

    //
    // Receive
    //
    TcpReceive( socket, gRecBuffer, elcount(gRecBuffer) );
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
