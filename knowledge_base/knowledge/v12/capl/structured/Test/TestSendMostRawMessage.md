# TestSendMostRawMessage

> Category: `Test` | Type: `function`

## Syntax

```c
long TestSendMostRawMessage(long aDestinationAddress, long aRType, BYTE aMsgData[], dword aMsgDataLength, dword aTimeout);
```

## Description

This function immediately sends a MOST raw control message with the specified data and waits for the associated Tx acknowledgment from the recipient. The AckNack bit is evaluated and the return value specifies whether the creation and sending of the message was successful or not.

The first signature specifies the message data by a byte array, the second uses a string to describe the data bytes as a hex dump.

## Return Values

-6: Parse Error; on specification of a message data description string that contains other characters than hexadecimal digits

## Availability

| Since Version |
|---|
