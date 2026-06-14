# Iso11783IL_OPGetVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetVersion( ); // form 1
long Iso11783IL_OPGetVersion( byte extendedVersions ); // form 2
long Iso11783IL_OPGetVersion( dbNode implement, byte extendedVersions ); // form 3
```

## Description

The function requests the stored object pools from the Virtual Terminal. A Get Versions command or a Extended Get Versions command is sent to the Virtual Terminal. If a response from the Virtual Terminal is received, the callback function Iso11783IL_OPOnResponse is called.

## Parameters

| Name | Description |
|---|---|
| extendedVersions | kind of versions to query. To get extended versions a VT version 5 or higher is necessary. 0: get standard version strings (7 characters) 1: get extended version strings (32 characters) |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPGetVersion( 
);

[...]

void Iso11783IL_OPOnResponse( dword handle, pg VTtoECU 
 response ) {
  switch(response.BYTE(0)) {
  case 224:
    // handle GetVersions response here
    break;
  case 211:
    // handle Extended Get Versions response here
    break;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 9.0: form 3 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3) | ✔ (form 3) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3) | ✔ (form 3) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
