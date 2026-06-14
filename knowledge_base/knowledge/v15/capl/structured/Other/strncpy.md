# strncpy

> Category: `Other` | Type: `function`

## Syntax

```c
void strncpy(char dest[], char src[], long max);
```

## Description

This function copies src to dest. max indicates the size of dest in bytes. The function ensures that there is a terminating '\0'. Thus, a maximum of max-1 bytes are copied.

## Parameters

| Name | Description |
|---|---|
| dest | Destination buffer |
| src | Source string |
| max | Is used to determine the maximum number of copied bytes.Must not be larger than the size of dest. A maximum of max-1 bytes are copied. If src is shorter than that, bytes are only copied until a terminating '\0' is encountered. |

## Return Values

—

## Example

```c
variables {
   char s1[7] = "Vector";
   char s2 [32];
}
on key 'z'
{                                 Output to the Write-Window:
   strncpy (s2,s1,elcount(s2));
   write ("Result: %s",s2);       Result: Vector
}
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
