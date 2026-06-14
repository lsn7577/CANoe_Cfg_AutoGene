# mbstrstr, mbstrstr_off

> Category: `Other` | Type: `function`

## Syntax

```c
long mbstrstr(char s1[], char s2[]);
long mbstrstr_off(char s1[], long offset, char s2[]);
```

## Description

Searches in s1 for s2.

## Parameters

| Name | Description |
|---|---|
| s1 | First string |
| s2 | Second string |
| offset | Offset in s1 in characters at which the search shall be started |

## Return Values

First position in characters of s2 in s1, or -1 if s2 is not found in s1.

## Example

```c
long pos;
char s[50] = "'Tür' is german for 'door'";
pos = mbstrstr(s, "german");
write("%d", pos); // 9
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
