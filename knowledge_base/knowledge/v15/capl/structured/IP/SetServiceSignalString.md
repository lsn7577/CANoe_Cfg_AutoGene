# SetServiceSignalString

> Category: `IP` | Type: `function`

## Syntax

```c
long SetServiceSignalString(serviceSignalString qualifier, char buffer []); // form 1
long SetServiceSignalString(char qualifier [], char buffer []); // form 2
```

## Description

Sets the string value of a Service Signal. The function automatically appends the respective byte order mark (BOM) depending on the data type (UTF8 or UTF16).

## Parameters

| Name | Description |
|---|---|
| qualifier | Qualifier of the Service Signal. |
| buffer[] | Data buffer for the value of the Service Signal. |

## Example

Note

The service qualifier is specified without a leading $ sign.

```c
on key 's'
{
SetServiceSignalString(DemoDatabase::PACKAGE1::PACKAGE2::Service1::1::2::Event1::StringValue,"Hello World");
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
