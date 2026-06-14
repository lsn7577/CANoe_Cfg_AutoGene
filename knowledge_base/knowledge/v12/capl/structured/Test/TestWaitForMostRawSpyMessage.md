# TestWaitForMostRawSpyMessage

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostRawSpyMessage(long aSourceAddress, long aDestinationAddress, long aRType, BYTE aMsgData [], dword aMsgDataLength, dword aTimeout);
```

## Description

This function waits for the occurrence of the specified MOST raw spy control message. Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Return Values

-6: Parse Error; on specification of a message data description string that contains other characters than hexadecimal digits or wildcards ("_").

## Availability

| Since Version |
|---|
