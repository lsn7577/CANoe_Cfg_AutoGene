# writeToLogEx

> Category: `Other` | Type: `function`

## Syntax

```c
void writeToLogEx(char format[], ...);
```

## Description

Writes an output string to an ASCII logging file. Write is based on the C function printf.

The compiler cannot check the format string. Illegal format entries will lead to undefined results. Different to the writeToLog function, neither comment characters ("//") nor time stamps will be printed at the beginning of a line.

## Return Values

—

## Example

```c
// write marker with current date and time to logging file
void MarkLogFileWithTimeString(void)
{
char timeBuffer[64];
getLocalTimeString(timeBuffer);
writeToLogEx("===> %s",timeBuffer);
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
