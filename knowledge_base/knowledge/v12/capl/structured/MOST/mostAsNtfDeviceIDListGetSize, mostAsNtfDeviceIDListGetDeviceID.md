# mostAsNtfDeviceIDListGetSize, mostAsNtfDeviceIDListGetDeviceID

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfDeviceIDListGetSize(long fblockID, long instID, long functionID)
```

## Description

The function makes it possible to output the list of all notification clients registered with the function (functionID). Functionality is similar to command message FBlock.Notification.Get(functionID).

The notification matrix can be read out with the function without sending a respective message.

## Return Values

See error codes

## Availability

| Since Version |
|---|
