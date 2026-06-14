# OnStationAttributeTrigger

> Category: `Car2x` | Type: `function`

## Syntax

```c
void OnStationAttributeTrigger(char attributeName[]);
```

## Description

This callback is called when the following three conditions are met:

This callback is intended to define a reaction on triggerable attributes of a scenario station assigned to the calling CAPL node only. If you want only react on a attribute triggering of all stations in the scenario, please use OnStationAttributeTriggerAll callback function instead.

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

| Since Version |
|---|
