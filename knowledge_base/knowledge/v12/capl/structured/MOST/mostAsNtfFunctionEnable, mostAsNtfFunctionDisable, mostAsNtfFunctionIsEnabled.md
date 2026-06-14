# mostAsNtfFunctionEnable, mostAsNtfFunctionDisable, mostAsNtfFunctionIsEnabled

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfFunctionEnable(long functionID, char cbSendStatus[])
```

## Description

mostAsNtfFunctionEnable() enables the notification service for a function. The notification service must be enabled with mostAsNtfEnable() for the function block beforehand.

The service must have the name of a CAPL function that generates and sends the status message of the properties. This is necessary, so that the service can send the current value of the properties with the FBlock.Notification.Set(SetFunction/SetAll) message to the client when registering a client (see MOST Specification 2.3 Section 2.3.12).

The CAPL function must be defined by the user and display the following signature:

or

The function must generate and send the status message to the destAdr address. If the status message could be sent, the function has to return the value 0. Otherwise it must report it to the notification service with the return value -1. The service then sends an error message (FBlock.Function.Error(0x41)) to the client instead of the status message.

mostAsNtfFunctionDisable() disables the notification service for the function.

mostAsNtfFunctionIsEnabled() returns 1, if the notification service is enabled for the function.

Database support:

The special value functionID=-1 triggers the execution of the CAPL function for all MOST functions from the function catalog meeting the following criteria:

## Return Values

See error codes

## Availability

| Since Version |
|---|
