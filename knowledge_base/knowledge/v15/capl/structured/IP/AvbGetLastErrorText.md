# AvbGetLastErrorText

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbGetLastErrorText(dword bufferLength, char buffer[]);
```

## Description

Function to retrieve the last error which occurs in the AVB IL as string.

The call of the AvbGetLastErrorText function does not reset the saved error text.

## Parameters

| Name | Description |
|---|---|
| bufferLength | Number of characters. |
| buffer | Buffer receiving the error text. |

## Return Values

Number of copied characters.

## Example

```c
char buffer[1024];
dword listenerHandle;

// open a listener
listenerHandle = AvbOpenListener();

// check if last function was executed successfully
if ((AvbGetLastErrorText(elcount(buffer), buffer)) != 0)
{
  write("AVB IL error occurred: %s", buffer);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
