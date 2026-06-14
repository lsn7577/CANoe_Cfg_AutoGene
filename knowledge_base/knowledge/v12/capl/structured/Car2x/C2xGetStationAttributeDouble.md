# C2xGetStationAttributeDouble

> Category: `Car2x` | Type: `function`

## Syntax

```c
float C2xGetStationAttributeDouble(char[] attributeName); // form 1
```

## Description

This function return the actual value of the floating point typed scenario attribute. Form1 of the function returns values of an attributes of the calling (current) station. Form2 allows to get values of all attributes of any station in the scenario, even if the scenario station does not have an assigned databasis node.

## Return Values

The floating point value of the attribute at the time of function call.

## Example

```c
void OnStartScenario()
{
  write("OnStartScenario - Station Speed = %f",   C2xGetStationAttributeDouble("Speed"));
}

void OnStationAttributeTrigger(char attrName[])
{
if (strncmp(attrName,"Speed",strlen(attrName)) == 0)
{
      write("%f sec : Speed = %f",
        TimeNowNS()/1e9 ,
        C2xGetStationAttributeDouble("Speed"));
    }
}

on key 'c'
{
write("OnStartScenario - Station Latitude = %f", C2xGetStationAttributeDouble("Latitude"));
write("OnStartScenario - Station Longitude = %f", C2xGetStationAttributeDouble("Longitude"));
}
```

## Availability

| Since Version |
|---|
