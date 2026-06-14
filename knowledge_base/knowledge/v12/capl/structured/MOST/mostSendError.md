# mostSendError

> Category: `MOST` | Type: `function`

## Syntax

```c
mostSendError_Code (mostAmsMessage * msgcmd, byte code)
```

## Description

Generates and sends an error message directly based on a received command message.

The various signatures make it easy to transfer the most common error codes with their ancillary information.

Any wildcard InstId in the command message is transferred to a concrete value in the error message with the help of the device’s Local FBlock list.

## Return Values

—

## Availability

| Since Version |
|---|
