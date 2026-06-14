# <OnC2xTransmitPacket>

> Category: `Car2x` | Type: `function`

## Syntax

```c
<OnC2xTransmitPacket>(packet);
```

## Description

This callback is invoked before a database defined packet is transmitted (by this network node).

Within this callback the Token functions from the Packet API and all Signal functions from the Car2x IL API can be used.

Modifications are persistent between invocations of the callback.

When using the form 2 of the callback it is possible to skip the current transmission by returning a 0.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the packet |

## Return Values

Form 1: —

## Availability

| Since Version |
|---|
