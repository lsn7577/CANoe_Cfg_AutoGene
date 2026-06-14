# C2xGetLastErrorText

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetLastErrorText( dword bufferSize, char[] buffer );
```

## Description

Gets the error code description of the last called C2x... function.

## Parameters

| Name | Description |
|---|---|
| bufferSize | Size of buffer in which the description text is copied |
| buffer | Buffer in which the description text is copied |

## Return Values

Number of copied bytes.

## Example

```c
char error[100];
long value;
long packetHandle;

value = C2xGetTokenInt( packetHandle, "eth", "type" );
if (C2xGetLastError() == 0)
{
  write("Ethernet Type is 0x%x", value );
}
else
{
  C2xGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
