# OnStartScenario

> Category: `Car2x` | Type: `function`

## Syntax

```c
void OnStartScenario();
```

## Description

This callback is called at the time when the scenario start was triggered:

## Return Values

—

## Example

```c
void OnStartScenario()
{
  write("Station '%NODE_NAME%': %f sec - OnStartScenario was called" , TimeNowNS()/1e9);
  write("Station '%NODE_NAME%': OnStartScenario - Station Speed = %f", C2xGetStationAttributeDouble("Speed"));
}
```

## Availability

| Since Version |
|---|
