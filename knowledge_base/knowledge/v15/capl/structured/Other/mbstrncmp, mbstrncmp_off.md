# mbstrncmp, mbstrncmp_off

> Category: `Other` | Type: `function`

## Syntax

```c
long mbstrncmp(char s1[], char s2[], long len); // form 1
long mbstrncmp(char s1[], char s2[], long s2offset, long len); // form 2
long mbstrncmp_off(char s1[], long s1offset, char s2[], long s2offset, long len); // form 3
```

## Description

This function compares s1 with s2 for a maximum of len characters.

If they are identical the functional result is 0. If s1 is less than s2 the result is -1, else +1.

Comparison starts in s1 at s1offset (form 3) and in s2 at s2offset (form 2 and form 3).

## Parameters

| Name | Description |
|---|---|
| s1 | First string |
| s2 | Second string |
| len | Maximum number of characters to compare |
| s1offset | Offset in s1 in characters |
| s2offset | Offset in s2 in characters |

## Example

```c
char s[50] = "'Tür' is the german word for 'door'.";
write("%d", mbstrncmp_off(s, 13, "german", 0, 6)); // 0
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
