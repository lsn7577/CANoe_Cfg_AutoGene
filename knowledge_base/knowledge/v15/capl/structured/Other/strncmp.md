# strncmp

> Category: `Other` | Type: `function`

## Syntax

```c
long strncmp(char s1[], char s2[], long len); // form 1
long strncmp(char s1[], char s2[], long s2offset, long len); // form 2
```

## Description

This function compares s1 with s2 for a maximum of len bytes.

If they are identical the functional result is 0. If s1 is less than s2 the result is -1, else +1.

Form 2 starts the comparison in s2 at the specified offset.

## Parameters

| Name | Description |
|---|---|
| s1 | First string |
| s2 | Second string |
| s2offset | Offset in s2 in bytes |
| len | Maximum number of bytes to compare |

## Example

```c
on key 's'
{
char s1[7] = "Vector";
char s2[7] = "Vector";
if(strncmp(s1,s2,strlen(s1)))
write("not equal");
else
write("equal");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All: form 1 7.0: form 2 | All: form 1 7.0: form 2 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
