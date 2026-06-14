# C2xGetStationSubAttributeDouble

> Category: `Car2x` | Type: `function`

## Syntax

```c
float C2xGetStationSubAttributeDouble(char[] attributeName, char[] subAttributeName); // form 1
float C2xGetStationSubAttributeDouble(char[] stationName, char[] attributeName, char[] subAttributeName); // form 2
```

## Description

This function returns the actual value of the floating point typed scenario sub-attribute. Form1 of the function returns values of an attribute of the calling (current) station. Form2 allows to get values of all sub-attributes of any station in the scenario, even if the scenario station does not have an assigned databasis node.

## Parameters

| Name | Description |
|---|---|
| stationName | Scenario station name |
| attributeName | Name of the scenario attribute which belongs to the scenario station specified by stationName parameter |
| subAttributeName | Name of the scenario sub-attribute which belongs to the scenario station attribute specified by attributeName parameter |

## Return Values

The floating point value of the attribute at the time of function call.

## Example

```c
void OnStartScenario()
{
  write("OnStartScenario - Station Sub Attribute = %f", C2xGetStationSubAttributeDouble("MyAttribute", "MySubAttribute"));
  write("OnStartScenario - Station Sub Attribute = %f", C2xGetStationSubAttributeDouble("Station1","MyAttribute", "MySubAttribute"));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0: form 1, 2 | — | — | — | 5.0: form 1, 2 |
| Restricted To | — | Car2x: form 1 Car2x, Testnodes: form 2 | — | — | — | Car2x: form 1 Car2x, Testnodes: form 2 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
