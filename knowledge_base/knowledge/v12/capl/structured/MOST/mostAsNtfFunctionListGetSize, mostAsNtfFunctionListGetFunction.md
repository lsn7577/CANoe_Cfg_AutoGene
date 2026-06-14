# mostAsNtfFunctionListGetSize, mostAsNtfFunctionListGetFunction

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfFunctionListGetSize(long deviceID, long fblockID, long instID)
```

## Description

The function makes it possible to output the list of all functions in which the notification client (deviceID) is registered. Functionality is similar to command message FBlock.NotificationCheck.Get(deviceID).

The notification matrix can be read out with the function without sending a respective message.

## Return Values

See error codes

## Availability

| Since Version |
|---|
