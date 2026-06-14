# swapWord, swapInt, swapDWord, swapLong, swapInt64, swapQWord

> Category: `Other` | Type: `function`

## Syntax

```c
word swapWord(word x); // form 1
int swapInt(int x); // form 2
dword swapDWord(dword x); // form 3
long swapLong(long x); // form 4
int64 swapInt64(int64 x); // form 5
qword swapQWord(qword x); // form 6
```

## Description

Swaps bytes of parameters. CAPL arithmetics follows the "little-endian-format" (Intel). The swap-functions serve for swapping bytes for the transition to and from the "big-endian-format" (Motorola).

## Return Values

Value with swapped bytes.

## Example

```c
bigEndian = swapInt(1234); // create constant 1234 for Motorola processors
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All: form 1-4 8.5: form 5, 6 | All: form 1-4 8.5: form 5, 6 | 13.0 | 13.0 | 14 | 1.0: form 1-4 2.0: form 5, 6 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
