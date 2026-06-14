# C2xGetStationAttributeInt64

> Category: `Car2x` | Type: `function`

## Syntax

```c
int64 C2xGetStationAttributeInt64(char[] attributeName); // form 1
int64 C2xGetStationAttributeInt64(char[] stationName, char[] attributeName); // form 2
```

## Description

This function returns the actual value of the integer-typed scenario attribute. Form 1 of the function returns values of an attribute of the calling (current) station. Form 2 allows to get values of all attributes of any station in the scenario, even if the scenario station does not have an assigned database node.

## Parameters

| Name | Description |
|---|---|
| stationName | Scenario station name. |
| attributeName | Name of the scenario attribute which belongs to the scenario station specified by stationName parameter. |

## Return Values

The integer value of the attribute at the time of function call.

## Example

```c
void OnStartScenario()
{
write("OnStartScenario - Doors locked = %d", C2xGetStationAttributeInt64("MyAttrDoorLocked"));
write("OnStartScenario - LeftTurnAllowed = %d", C2xGetStationAttributeInt64("TrafficLightStation","Lane1State"));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0: form 1, 2 | — | — | — | 3.0: form 1, 2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
