# timeDiff

> Category: `Other` | Type: `function`

## Syntax

```c
long timeDiff(message m1, NOW); // from 1
long timeDiff(message m1, message m2); // from 2
```

## Description

Time difference between messages or between a message and the current time in ms (msg2 - msg1 or now - msg1). Starting with CANalyzer 2.xx this difference can be calculated directly (Units of 10 microseconds).

## Return Values

Time difference in ms.

## Example

```c
diff = timeDiff(m100, now); // CANalyzer 1.x & 2.x
diff = this.time - m100.time; // CANalyzer 2.xx
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
