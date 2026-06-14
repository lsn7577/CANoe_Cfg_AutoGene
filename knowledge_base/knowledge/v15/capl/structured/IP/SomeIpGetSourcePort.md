# SomeIpGetSourcePort

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetSourcePort ( dword messageHandle );
```

## Description

This function returns the source port (UDP/TCP).

## Parameters

| Name | Description |
|---|---|
| Note This function can only be called within the OnSomeIpMessage callback function. |  |

## Example

```c
void OnSomeIpMessage( DWORD messageHandle )
{
  DWORD srcPort       = 0;
  LONG  errorCode     = 0;
  LONG  errorOccured  = 0;

  // get data from SOME/IP message
  if((srcPort = SomeIpGetSourcePort(messageHandle)) == 0)
  {
    // check if last function was executed correct
    if((errorCode = SomeIpGetLastError()) != 0)
    {
      write("SOME/IP IL error occured: Error code: %d", errorCode);
      errorOccured = 1;
    } // if
  } // if

  if(errorOccured == 0)
  {
    write("SOME/IP message from Source Port %d received",srcPort);
  } // if
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
