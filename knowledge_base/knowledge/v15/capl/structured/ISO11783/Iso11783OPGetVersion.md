# Iso11783OPGetVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetVersion( dword ecuHandle );
long Iso11783OPGetVersion( dword ecuHandle, byte extendedVersions );
```

## Description

The function requests the stored object pools from the Virtual Terminal. A Get Version command or a Get Extended Version command is sent to the Virtual Terminal. If a response from the Virtual Terminal is received, the callback function Iso11783OPOnResponse is called.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| extendedVersions | Kind of versions to query. To get extended versions a VT version 5 or higher is necessary. 0: get standard version strings (7 characters) 1: get extended version strings (32 characters) |

## Return Values

0 or error code

## Example

```c
Iso11783OPGetVersion(handle
);

[...]

void Iso11783OPOnResponse( dword handle, pg VTtoECU 
 response ) {
  switch(response.BYTE(0)) {
  case 224:
    // handle GetVersion response here
    break;
  case 211:
    // handle Get Extended Version response here
    break;
  }
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
