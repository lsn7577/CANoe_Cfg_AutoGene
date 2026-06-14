# vFlashGetLastErrorMessage

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashGetLastErrorMessage();
```

## Description

Requests a call to the CAPL callback vFlashErrorMessage containing information on the error that occurred.

## Return Values

—

## Example

```c
  // ...Error occurred...
  vFlashGetLastErrorMessage();
}

void vFlashErrorMessage(char errorMsg[])
{
  write("Error %s", errorMsg);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP3 + DLL 2.7.3100 | — | — | — | 2.0 SP2 + DLL 2.7.3100 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
