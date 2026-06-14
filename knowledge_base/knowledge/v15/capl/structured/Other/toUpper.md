# toUpper

> Category: `Other` | Type: `function`

## Syntax

```c
char toUpper(char c); // form 1
void toUpper(char dest[], char source[], dword bufferSize); // form 2
```

## Description

Transforms a character or string to upper case. Only characters a-z and A-Z are supported.

## Parameters

| Name | Description |
|---|---|
| c | Character to be transformed. |
| source | String to be transformed. |
| dest | Destination buffer for the transformed string. |
| bufferSize | Size of the destination buffer. |

## Return Values

Upper case of the character (form 1).

## Example

```c
char buffer[20];
toUpper(buffer, "Vector", elcount(buffer)); // buffer contains "VECTOR"
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 | 7.2 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
