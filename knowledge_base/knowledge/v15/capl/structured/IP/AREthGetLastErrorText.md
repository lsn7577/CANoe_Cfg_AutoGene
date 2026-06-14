# AREthGetLastErrorText

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthGetLastErrorText( dword bufferLength, CHAR buffer[] );
```

## Description

Interface to retrieve the last error which occurs in the AUTOSAR Eth IL as string.

If the last called function has been successfully executed, the value 0 is returned. The call of the AREthGetLastErrorText function does not reset the saved error text.

## Parameters

| Name | Description |
|---|---|
| bufferLength | Number of characters |
| buffer | Buffer receiving the error text |

## Return Values

Number of copied characters.

## Example

```c
char buffer[1024];

// resume sending messages
AREthILControlResume();

// check if last function was executed correct
if((AREthGetLastErrorText(elcount(buffer),buffer)) != 0)
{
  write("AUTOSAR Eth IL error occurred: %s", buffer);
} // if
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
