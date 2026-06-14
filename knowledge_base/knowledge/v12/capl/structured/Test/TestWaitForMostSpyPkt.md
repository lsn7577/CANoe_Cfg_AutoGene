# TestWaitForMostSpyPkt

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostSpyPkt(long aSourceAddress, long aDestinationAddress, char aPktDataDesc[], long aInstanceID, dword aTimeout);
```

## Description

Waits for the occurrence of the specified MOST (spy) packet. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

The first and third signatures are exclusively suited to set up wait conditions for packets having function catalog format, whereas the other signatures also allow the definition of raw packets.

Spy packets, but also node packets (with any direction) will resolve a wait condition set up by this function, since CANoe does not double an incoming packet on a channel that has asynchronous spy activated.

## Parameters

| Name | Description |
|---|---|
| Note For parameters aSourceAddress, aDestinationAddress, and aInstanceId the following applies: If -1 is given, the corresponding field can get any value. This is also the standard for not explicit set values. |  |

## Return Values

-6: Parse Error; on specification of a packet description string, that can’t be resolved with the XML function catalog or that is flawed

## Availability

| Since Version |
|---|
