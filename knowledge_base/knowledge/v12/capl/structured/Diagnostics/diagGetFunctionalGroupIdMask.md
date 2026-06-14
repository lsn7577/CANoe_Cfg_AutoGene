# diagGetFunctionalGroupIdMask

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
dword diagGetFunctionalGroupIdMask ()
```

## Description

Determines the CAN ID mask in order to be able to filter out CAN messages sent by the diagnostic tester as functional requests.

If the functional group is not specified, the destination set with diagSetTarget is used.

## Return Values

The value returned must be logically ANDed with the ID of a received CAN message. If the result is the same as the Group ID, this is a functional request.

## Availability

| Since Version |
|---|
