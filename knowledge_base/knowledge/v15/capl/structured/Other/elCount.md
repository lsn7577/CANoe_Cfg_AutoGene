# elCount

> Category: `Other` | Type: `function`

## Syntax

```c
long elcount(...); // if used with arrays which are function parameters
dword elcount(...); // in all other cases
```

## Description

Determines the number of elements of an array.

## Return Values

Number of elements.

## Example

```c
void bsp(int ar[]) {
int i;
for(i=0; i < elCount(ar); i++)
...
}

void bsp2(byte ar[][]) {
int i, j;
for(j=0; j < elCount(ar); j++ )
for(i=0; i<= elCount(ar[j]); i++ )
...
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
