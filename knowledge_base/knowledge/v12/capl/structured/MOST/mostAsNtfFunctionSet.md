# mostAsNtfFunctionSet

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfFunctionSet(long deviceID, long fblockID, long instID, long functionID)
```

## Description

Registers a notification client in the notification matrix. Functionality is similar to command message FBlock.Notification.Set(SetFunction, deviceID, functionID).

The notification matrix can be written with the function without sending a respective message.

The notification matrix is deleted on NetOn and if the network status changes to ConfigNotOk.

## Return Values

See error codes

## Availability

| Since Version |
|---|
