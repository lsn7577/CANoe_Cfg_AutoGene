# mostAsNtfShdFunctionEnable, mostAsNtfShdFunctionDisable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfShdFunctionEnable(long fblockId, long instId, long functionId)
```

## Description

mostAsNtfShdFunctionEnable() registers a MOST function with the notification shadow service. As soon as the specified function block (fblockId, instId) appears in the bus registry of the simulated device, the notification shadow service enters the simulated device in the notification matrix of the function block, i.e., it sends the FBlockId.InstId.Notification.Set(SetFunction, functionId) message.

mostAsNtfShdFunctionDisable() removes a MOST function from the notification shadow service.

## Return Values

See error codes

## Availability

| Since Version |
|---|
