# FSIL_OnCurrentDirectoryChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void FSIL_OnCurrentDirectoryChanged( dword clientAddress, char currentDirectory[]);
```

## Description

Is called from the FS IL if a client has changed its current directory.

## Parameters

| Name | Description |
|---|---|
| clientAddress | Address of the File Server client which has changed its current directory. |
| currentDirectory | Path of the current directory (relative to the root directory). |

## Return Values

—

## Example

```c
void FSIL_OnCurrentDirectoryChanged( dword clientAddress, char currentDirectory[])
{
  write("Client with address %u has changed it current directory to '%s'", clientAddress, currentDirectory);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
