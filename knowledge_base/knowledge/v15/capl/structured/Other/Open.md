# Open

> Category: `Other` | Type: `function`

## Syntax

```c
file(char [] filename, dword access, dword mode); // form 1
file(char [] filename, dword access, dword mode, dword fileEncoding); // form 2
```

## Description

This function opens the file named filename.

If access = 0, the file is opened for write access; if access = 1 the file is opened for read access.

If mode = 0 the file is opened in text mode; if mode = 1 the file is opened in binary mode.

## Parameters

| Name | Description |
|---|---|
| filename | The name of the file |
| access | 0 for write access, 1 for read access |
| mode | 0 for text mode, 1 for binary mode |
| fileEncoding | Identifier of the Microsoft code page that is used to encode the file. |

## Return Values

— (constructor)

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0: form 1 12.0: form 2 | 7.0: form 1 12.0: form 2 | 13.0 | — | 14 | 1.0: form 1 4.0: form 2 |
| Restricted To | CAN | CAN | CAN | — | CAN | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
