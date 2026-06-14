# MediaGetLastError

> Category: `Media` | Type: `function`

## Syntax

```c
dword MediaGetLastError();
```

## Description

Retrieves the calling CAPL program’s last-error code value of the Media API. This code represents a Windows HRESUL value typically in the value ranges reserved for the Windows Media Foundation (see error codes).

## Return Values

Error code

## Example

```c
dword retVal;
dword listenerHandle;
// open a listener
listenerHandle = AvbOpenListener();

// check if last function was successfully executed
if ((retVal = AvbGetLastError()) != 0)
{
  write("AVB IL error occured: Error code: %d", retVal);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2 | 13.0 | — | — | — |
| Restricted To | — | Ethernet | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | — |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | — |
| CANoe System and Communication Setup | N/A | — | ✔ | — | — | — |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | — |
| 32-Bit | — | ✔ | ✔ | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | — | — | — |
