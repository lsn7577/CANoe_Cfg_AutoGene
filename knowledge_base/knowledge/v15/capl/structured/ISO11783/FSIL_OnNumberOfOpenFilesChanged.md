# FSIL_OnNumberOfOpenFilesChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void FSIL_OnNumberOfOpenFilesChanged( dword clientAddress, dword numberOfOpenFiles)
```

## Description

Is called from the FS IL if a client has opened or closed a file or directory.

## Parameters

| Name | Description |
|---|---|
| clientAddress | Address of the File Server client which has opened or closed a file or directory. |
| numberOfOpenFiles | Current number of files or directories which are opened by the File Server client. |

## Return Values

—

## Example

```c
void FSIL_OnNumberOfOpenFilesChanged( dword clientAddress, dword numberOfOpenFiles)
{
  write("Client with address %u has %u open files", clientAddress, numberOfOpenFiles);
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
