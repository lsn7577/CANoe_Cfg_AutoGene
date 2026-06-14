# AfdxGetLastErrorText

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetLastErrorText( dword bufSize, char[] buffer );
```

## Description

Gets the error code description of the last called Afdx... function.

## Parameters

| Name | Description |
|---|---|
| bufSize | Size of buffer in which the description text is copied. |
| buffer | Buffer in which the description text is copied. |

## Return Values

Number of copied bytes.

## Example

```c
char error[100];
long value;
long packetHandle;

value = AfdxGetTokenInt( packetHandle, "eth", "type" );
if (AfdxGetLastError() == 0)
{
  write("Ethernet Type is 0x%x", value );
}
else
{
AfdxGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
