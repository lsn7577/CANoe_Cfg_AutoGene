# mostAsNtfFunctionClearAll

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfFunctionClearAll(long deviceID, long fblockID, long instID)
```

## Description

Clears notification client entries from the notification matrix (deviceID >= 0). Functionality is similar to command message FBlock.Notification.Set(ClearAll, deviceID).

The notification matrix can be written with the function without sending a respective message.

## Return Values

See error codes

## Availability

| Since Version |
|---|
