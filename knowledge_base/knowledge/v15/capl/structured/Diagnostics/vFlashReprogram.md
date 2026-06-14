# vFlashReprogram

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashReprogram();
```

## Description

Starts the flashing procedure. The progress will be indicated by calls to the optional callback vFlashProgramProgressCallback. The procedure has finished when CAPL callback vFlashReprogramCompleted is called.

Note: This event-driven API is only needed outside of test modules or test units.

## Example

```c
  FlashReprogram();
}
void vFlashProgramProgressCallback(dword progressInPercent, dword remainingTimeInS)
{
  // Do not print on every progress callback, but only in 10% steps
  DWORD sProgress = 0;
  if (progressInPercent < sProgress)
    sProgress = 0; // reset progress stored
  if (progressInPercent < 100 && (progressInPercent - sProgress) >= 10)
  {
    write("Progress: %3u%%, %us remaining", progressInPercent, remainingTimeInS);
    sProgress = progressInPercent - (progressInPercent % 10);
  }
}

void vFlashReprogramCompleted(long status)
{
  write("Reprogramming completed with status %d", status);
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
