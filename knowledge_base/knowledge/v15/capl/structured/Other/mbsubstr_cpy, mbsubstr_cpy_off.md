# mbsubstr_cpy, mbsubstr_cpy_off

> Category: `Other` | Type: `function`

## Syntax

```c
void mbsubstr_cpy(char dest[], char src[], long srcStart, long len);
void mbsubstr_cpy_off(char dest[], long destOffset, char src[], long srcStart, long len);
```

## Description

mbsubstr_cpy copies a substring of src to dest. len indicates the number of characters that shall be copied; use -1 to indicate that as much shall be copied into dest as will fit (maximum until the end of src). The function ensures that there is a terminating 0 byte; but in contrast to substr_cpy/substr_cpy_off, that byte is not counted into len.

mbsubstr_cpy_off overwrites characters in the destination buffer starting at the character offset destOffset.

## Parameters

| Name | Description |
|---|---|
| dest | Destination buffer |
| src | Source string |
| srcStart | Start index in characters in src of substring |
| len | Number of characters to be copied, or -1 to copy as much as possible |
| destOffset | Offset in characters into the destination buffer |

## Return Values

—

## Example

```c
char s1[50] = "eine grüne "; // german for 'a green'
char s2[20] = "schöne Türen"; // german for 'beautiful doors'
mbsubstr_cpy_off(s1, 11, s2, 7, 3);
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
