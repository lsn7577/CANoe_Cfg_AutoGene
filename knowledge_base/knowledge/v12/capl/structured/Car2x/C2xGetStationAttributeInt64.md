# C2xGetStationAttributeInt64

> Category: `Car2x` | Type: `function`

## Syntax

```c
int64 C2xGetStationAttributeInt64(char[] attributeName); // form 1
```

## Description

This function returns the actual value of the integer-typed scenario attribute. Form 1 of the function returns values of an attribute of the calling (current) station. Form 2 allows to get values of all attributes of any station in the scenario, even if the scenario station does not have an assigned database node.

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

| Since Version |
|---|
