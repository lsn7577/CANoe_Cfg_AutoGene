# vFlashUnloadProject

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashUnloadProject();
```

## Description

Unloads the current vFlash project. The CAPL callback vFlashUnloadProjectCompleted will be called when the unloading completed and further API calls are possible.

Note: This event-driven API is only needed outside of test modules or test units.

## Return Values

—

## Example

```c
  // ...
  vFlashUnloadProject();
}

void vFlashUnloadProjectCompleted(enum vFlashStatusCode statusCode)
{
  write("Unloading project completed, another project can be loaded.");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 + DLL 3.5.100 | — | — | — | 2.2 SP2 + DLL 3.5.100 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
