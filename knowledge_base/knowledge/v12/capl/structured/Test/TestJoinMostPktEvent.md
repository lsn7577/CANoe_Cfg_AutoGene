# TestJoinMostPktEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinMostPktEvent(long aSourceAddress, long aDestinationAddress, char aPktDataDesc[], long aInstanceID)
```

## Description

Adds an event condition for MOST packets to the current set of joined event conditions.

This function does not wait.

Note, that the first and third signatures are exclusively suited to set up wait condition events for packets having function catalog format, whereas the other signatures also allow the definition of raw packet events.

## Parameters

| Name | Description |
|---|---|
| Note For parameters aSourceAddress, aDestinationAddress, and aInstanceId the following applies: If -1 is given, the corresponding field can get any value. This is also the standard for not explicit set values. |  |

## Return Values

-6: Parse Error; on specification of a packet description string, that can’t be resolved with the XML function catalog or that is flawed.

## Availability

| Since Version |
|---|
