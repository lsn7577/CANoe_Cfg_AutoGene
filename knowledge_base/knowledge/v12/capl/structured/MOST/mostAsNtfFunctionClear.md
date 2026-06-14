# mostAsNtfFunctionClear

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfFunctionClear(long deviceID, long fblockID, long instID, long functionID)
```

## Description

Clears a notification client entry from the notification matrix. Functionality is similar to command message FBlock.Notification.Set(Clear, deviceID, functionID).

The notification matrix can be written with the function without sending a respective message.

## Return Values

See error codes

## Availability

| Since Version |
|---|
