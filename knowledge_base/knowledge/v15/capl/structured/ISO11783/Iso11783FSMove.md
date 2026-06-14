# Iso11783FSMove

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSMove( char sourcePath[], char destPath[], dword movemode );
```

## Description

The function moves, copies or deletes a file or directory.

## Parameters

| Name | Type | Description |
|---|---|---|
| sourcePath |  | Absolute file or directory source path |
| destPath |  | Absolute file or directory destination path or 0 to delete the file or directory specified in sourcePath |
| Bit | Value | Description |
| 0 | 01 | Action: copyAction: move |
| 1 | 1 | delete option: force |
| 2 | 1 | delete option: recursive |

## Return Values

0 or error code

## Example

```c
// Move
Iso11783FSMove( "\TEST.TXT", "\DIR1\TEST.TXT", 0x00 
 );

// Copy & Rename
Iso11783FSMove( "\TEST.TXT", "\DIR1\TEST2.TXT", 0x01 
 );

// Delete (even, if "TEST.TXT" 
 is read-only)
Iso11783FSMove( "\TEST.TXT", 0, 0x06 );
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
