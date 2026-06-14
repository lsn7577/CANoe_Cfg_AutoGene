# GetServiceSignalString

> Category: `IP` | Type: `function`

## Syntax

```c
long GetServiceSignalString(serviceSignalString qualifier, char buffer [], dword bufferLength); // form 1
long GetServiceSignalString(char qualifier [], char buffer [], dword bufferLength); // form 2
```

## Description

Reads the string value of a Service Signal.

## Parameters

| Name | Description |
|---|---|
| qualifier | Qualifier of the Service Signal. |
| buffer[] | Data buffer for the value of the Service Signal. |
| bufferLength | Length of the data buffer. |

## Example

Note

The service qualifier is specified without a leading $ sign.

```c
on key 'r'
{
  char buffer[255];
  GetServiceSignalString(DemoDatabase::PACKAGE1::PACKAGE2::Service1::1::2::Event1::StringValue, buffer, elcount(buffer));

  write("Actual value of Service Signal StringValue: %s",buffer);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2: form 1 9.0 SP4: form 2 | 13.0 | — | — | 2.1 SP3: form 1 9.0 SP4: form 2 |
| Restricted To | — | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
