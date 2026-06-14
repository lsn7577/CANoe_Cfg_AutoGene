# getSignalDescriptionForValue

> Category: `SignalAccess` | Type: `function`

## Syntax

```c
long getSignalDescriptionForValue(Signal signal, int64 rawValue, char buffer[], long bufferSize); // form 1
long getSignalDescriptionForValue(char signalNamel[], int64 rawValue, char buffer[], long bufferSize); // form 2
long getSignalDescriptionForValue(serviceSignalNumber signal, int64 rawValue, char buffer[], long bufferSize); // form 3
```

## Description

Retrieves the description for the value of a database signal. In this way, you can access the value table of the signal.

## Parameters

| Name | Description |
|---|---|
| signal | The signal (form 1). |
| rawValue | The value for which the description shall be retrieved. This must be the raw value, not the physical value. |
| buffer | String buffer which receives the value description. |
| bufferSize | Size of the buffer. |
| Note Signal Ambiguity You have to use further objects to identify the signal uniquely. They are: channel, database name (alias), node name and message name. The exact qualification syntax is:[Channel::][Database name (alias)::][Node::][Message::]Signal The order and completeness of the objects from right to left is important (see example). |  |

## Example

```c
char buffer[100]; long ret;
ret = getSignalDescriptionForValue(PowerTrain::Engine::GearBoxInfo::Gear, 1, buffer, elcount(buffer));
if (ret == 0) write("Description for value 1 is '%s'", buffer);
else write("Error getting description for value 1: %d", ret);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
