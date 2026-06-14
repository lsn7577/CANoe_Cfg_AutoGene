# OnStationAttributeTriggerAll

> Category: `Car2x` | Type: `function`

## Syntax

```c
void OnStationAttributeTriggerAll(char stationName[], char attributeName[]);
```

## Description

This callback is called when the following two conditions are met:

The purpose of this callback is to define a reaction on all triggerable attributes of all stations in the scenario. If you only want to react on the attribute triggering of the station’s own attributes only, please use OnStationAttributeTrigger callback function instead.

## Parameters

| Name | Description |
|---|---|
| stationName | Name of the scenario station |
| attributeName | Name of the scenario station attribute |

## Return Values

—

## Example

```c
void OnStationAttributeTriggerAll(char stationName[], char attributeName[])
{
    // For all trigger attributes of all stations in the scenario
    write("CAPL Node '%NODE_NAME%', Car2x/V2x station '%s', %f sec : OnStationAttributeTriggerAll called - Attribute '%s' = %f" ,
      stationName,
      TimeNowNS()/1e9 ,
      attributeName,
      C2xGetStationAttributeDouble(stationName, attributeName));

    // For concrete trigger attribute of a some known station "Station1"
    if (strncmp(stationName,"Station1",strlen(stationName)) == 0 &&
strncmp(attributeName,"Speed",strlen(attributeName)) == 0)
    {
      write("Car2x/V2x Station '%s', %f sec : OnStationAttributeTriggerAll called - Station1 Speed = %f",
        stationName,
        TimeNowNS()/1e9 ,
        C2xGetStationAttributeDouble(stationName, "Speed"));
    }
  }
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | — | — | — | 3.0 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
