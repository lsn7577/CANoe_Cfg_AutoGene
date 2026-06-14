# OnStationAttributeTrigger

> Category: `Car2x` | Type: `function`

## Syntax

```c
void OnStationAttributeTrigger(char attributeName[]);
```

## Description

This callback is called when the following three conditions are met:

This callback is intended to define a reaction on triggerable attributes of a scenario station assigned to the calling CAPL node only. If you want only react on a attribute triggering of all stations in the scenario, please use OnStationAttributeTriggerAll callback function instead.

## Parameters

| Name | Description |
|---|---|
| attributeName | Name of the scenario station attribute |

## Return Values

—

## Example

```c
void OnStationAttributeTrigger(char attrName[])
{
  long stationHandle;
  char stationName[200];
  stationHandle = C2xGetStationHandle("%NODE_NAME%");
  if (stationHandle != 0 && C2xGetStationName(stationHandle, elCount(stationName), stationName) == 0)
  {
    // For all attributes of this station
    write("CAPL Node '%NODE_NAME%', Car2x/V2x station '%s', %f sec : OnStationAttributeTrigger called - Attribute '%s' = %f" ,
      stationName,
       TimeNowNS()/1e9 ,
      attrName,
      C2xGetStationAttributeDouble(attrName));

    // For concrete attribute of this station
    if (strncmp(attrName,"Speed",strlen(attrName)) == 0)
    {
      write("Car2x/V2x Station '%s', %f sec : OnStationAttributeTrigger called - Station Speed = %f",
        stationName,
        TimeNowNS()/1e9 ,
        C2xGetStationAttributeDouble("Speed"));
    }
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
