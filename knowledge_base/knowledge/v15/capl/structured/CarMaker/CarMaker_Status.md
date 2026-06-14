# CarMaker_Status

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_Status( );
```

## Description

Retrieves the status of the CarMaker connection.

## Return Values

No connection
Connection is being built up
Connection established

## Example

```c
// get the current connection status
connState = CarMaker_Status();

if (gConnectionState != connState)
{
  //get detailed connection Info
  gConnectionState = connState;
  CarMaker_StatusText(connTextBuf, elcount(connTextBuf));

  if((gConnectionState & 0x10) != 0) // NOT connected...
  {
    msgSeverity = 3; // Error
  }
  if((gConnectionState & 0x20) != 0) // connecting...
  {
    msgSeverity = 2; // Warning
  }
  if((gConnectionState & 0x40) != 0) // connected...
  {
    msgSeverity = 1; // Information
  }
  writeLineEx(1, msgSeverity, "CarMaker connection status 0x%lx: \"%s\"", gConnectionState, connTextBuf);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | CarMaker | — | — | — | CarMaker |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
