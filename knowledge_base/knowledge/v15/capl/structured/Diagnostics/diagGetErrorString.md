# diagGetErrorString

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetErrorString (long errorCode, char bufferOut[], dword bufferLength)
```

## Description

Retrieves a text describing the error code.

## Parameters

| Name | Description |
|---|---|
| errorCode | Numeric error code |
| bufferOut | Output buffer |
| bufferLength | Output buffer size |

## Return Values

Length of the text in bufferOut.

## Example

```c
on key 't'
{
  long retValue;
  char buffer[200];
  if ( 0 > (retValue=diagSetTarget("UDS_Diagnostic_Services"))) 
  {
    diagGetErrorString(retValue, buffer, elcount(buffer));
    write("Error: %s", buffer);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | — | — | — | 2.0 |
| Restricted To | — | — | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
