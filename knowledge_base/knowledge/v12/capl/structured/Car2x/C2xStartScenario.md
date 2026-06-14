# C2xStartScenario

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xStartScenario(); // form 1
```

## Description

form 1

This function starts the scenario assigned to the current CANoe configuration immediately. The scenario can also be started manually in Scenario Manager Window. In both cases, the successful scenario start will be indicated by OnScenarioStart()callback function.

form 2

Starts the current scenario at specified geographical position (latitude, longitude) in specified direction (heading parameter). The original scenario will be transformed in the following way before the scenario starts:

1) All routes and stations in the scenario will be moved to a new geographical position in a way that following condition is met: start point of the route of the scenario station specified by stationName parameter is equal to geographical position specified in latitude and longitude parameters.

2) All routes and stations in the scenario will be rotated around the geographical position specified in latitude and longitude parameters until the route of the scenario station specified by stationName have the same direction as specified in the heading parameter.

Original scenario data transformations (moving and rotating) done by this function are active until the scenario stop.

## Return Values

1: Success

## Example

```c
Form 2:
on key 's'
{
  double lat = 48.8234237480101;
  double lon = 9.09433094246674;
  double heading = 45.0;
  if (C2xStartScenario("MyStation", lat, lon, heading) == 1)
  {
    write("Scenario started");
  }
}
```

## Availability

| Since Version |
|---|
