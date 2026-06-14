# Iso11783IL_FSGetVolumeInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSGetVolumeInfo( dword infoCount, dword retInfo[] );
```

## Description

This function returns information about the current volume. The current volume is the volume where the configuration is stored.

## Parameters

| Name | Description |
|---|---|
| infoCount | Number of elements in retInfo |
| Index | Description |
| 0 | Bit filled with valid elements, Bit 1 set = Index 1 is valid, ... |
| 1 | Total space of the volume in 512 byte blocks |
| 2 | Free space in 512 byte blocks |

## Example

```c
dword info[3];

Iso11783IL_FSGetVolumeInfo( elCount(info), info );
write( "Total 
 size %d blocks", info[1] );
write( "Free size 
 %d blocks", info[2] );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
