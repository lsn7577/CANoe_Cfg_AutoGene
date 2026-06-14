# mbstrncpy, mbstrncpy_off

> Category: `Other` | Type: `function`

## Syntax

```c
void mbstrncpy(char dest[], char src[], long len);
void mbstrncpy_off(char dest[], long destOffset, char src[], long len);
```

## Description

mbstrncpy function copies src to dest. len indicates the number of characters that shall be copied; use -1 to indicate that as much shall be copied into dest as will fit (maximum until the end of src). The function ensures that there is a terminating 0 byte; but in contrast to strncpy, that byte is not counted into len.

mbstrncpy_off overwrites characters in the destination buffer starting at the character offset destOffset.

## Parameters

| Name | Description |
|---|---|
| dest | Destination buffer |
| src | Source string |
| len | Number of characters to be copied, or -1 to copy as much as possible |
| destOffset | Offset in characters into the destination buffer |

## Return Values

—

## Example

```c
char s1[50] = "eine grüne "; // german for 'a green'
char s2[10] = "Türen"; // german for 'doors'
mbstrncpy_off(s1, 11, s2, 3);
write("%s", s1); // eine grüne Tür (german for 'a green door')
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP3 | 11.0 SP3 | 13.0 | — | 14 | 3.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
