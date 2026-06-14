# ltoa

> Category: `Other` | Type: `function`

## Syntax

```c
void ltoa(long val, char s[], long base);
```

## Description

The number val is converted to a string s. In this case, base indicates a number base between 2 and 36. s must be large enough to accept the converted number!

## Parameters

| Name | Description |
|---|---|
| val | Number to be converted. |
| s | String, which contains the converted number. |
| base | Number base. |

## Return Values

—

## Example

Result:

```c
char s1[9];
char s2[9];
ltoa(z,s1,2);
ltoa(z,s2,10);
write("z: %d s1= %s",z, s1);
write("z: %d s2= %s",z, s2);
...
z: 255 s1= 11111111
z: 255 s2= 255
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
