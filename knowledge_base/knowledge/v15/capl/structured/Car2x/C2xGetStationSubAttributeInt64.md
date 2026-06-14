# C2xGetStationSubAttributeInt64

> Category: `Car2x` | Type: `function`

## Syntax

```c
float C2xGetStationSubAttributeInt64(char[] attributeName, char[] subAttributeName); // form 1
float C2xGetStationSubAttributeInt64(char[] stationName, char[] attributeName, char[] subAttributeName); // form 2
```

## Description

This function returns the actual value of the integer-typed scenario sub-attribute. Form 1 of the function returns values of a sub-attribute of the calling (current) station. Form 2 allows to get values of all sub-attributes of any station in the scenario, even if the scenario station does not have an assigned database node.

## Parameters

| Name | Description |
|---|---|
| stationName | Scenario station name |
| attributeName | Name of the scenario attribute which belongs to the scenario station specified by stationName parameter |
| subAttributeName | Name of the scenario sub-attribute which belongs to the scenario station attribute specified by attributeName parameter |

## Return Values

The integer value of the attribute at the time of function call.

## Example

```c
void OnStartScenario()
{
  write("OnStartScenario - Station Sub Attribute = %d", C2xGetStationSubAttributeInt64("Events_EEBL1", " CauseCode"));
  write("OnStartScenario - Station Sub Attribute = %d", C2xGetStationSubAttributeInt64("Station1", "Events_EEBL1", " CauseCode"));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0: form 1, 2 | — | — | — | 5.0: form 1, 2 |
| Restricted To | — | Car2x: form 1 Car2x, Testnodes: form 3 | — | — | — | Car2x: form 1 Car2x, Testnodes: form 3 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
