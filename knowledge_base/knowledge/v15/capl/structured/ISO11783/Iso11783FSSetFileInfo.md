# Iso11783FSSetFileInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSSetFileInfo( dword fileHandle, dword infoCount, dword info[] );
long Iso11783FSSetFileInfo( char fileName[], dword infoCount, dword info[] );
```

## Description

This function sets file or directory attributes.

## Parameters

| Name | Type | Description |
|---|---|---|
| fileHandle |  | File or directory handle, see also Iso11783FSOpenFile |
| fileName |  | Name of file or directory |
| infoCount |  | Number of elements in info |
| Index |  | Description |
| 0 |  | bit field with valid elements, Bit 1 set = Index 1 is valid, ... |
| Bit | Value | Function |
| 1-2 | 013 | Read-only attribute ClearSetNo change |
| 3-4 | 013 | Hidden attribute ClearSetNo change |
| 5-6 | 013 | System attribute ClearSetNo change |
| 7-8 | 013 | Archive attribute ClearSetNo change |

## Return Values

0 or error code

## Example

```c
LONG handle;
dword info[2];

handle = Iso11783FSSetFileInfo( "\TEST.TXT", 0x00 );
if (handle > 0) {
  info[0] = 0x01; // Entry 1 is valid
  info[1] = 0x04; // Hide file
  if (Iso11783FSSetFileInfo( handle, elCount(info), info ) == 0) {
    write( "Changed attributes successfully" );
  }
  Iso11783FSCloseFile( handle );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
