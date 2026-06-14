# AREthCreateMessage

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthCreateMessage( dword messageId, dword requestId, dword protocolVersion, dword interfaceVersion, dword messageType, dword returnCode ); // form 1
```

## Description

This function is used to create a SOME/IP message that can then be sent with AREthOutputMessage or AREthPostMessage.

Form 1

If a FIBEX database is assigned to the CANoe configuration, a check is made to determine whether the message ID (messageId parameter) is contained in this database. If so, the payload is created according to the database description and initialized with 0. The length field in the SOME/IP message header is set automatically. If a corresponding message ID is not found in the database, only the SOME/IP message header is created. In this case, the payload must be created with AREthSetData.

Form 2

During creation, the message header length is taken from the data stream specified in the buffer parameter. In so doing, incorrect length values are not corrected.

If the message is successfully accessed later with a AREthGetValue... or AREthSetValue... function, the length is adapted in the message, if necessary, if a FIBEX database is assigned to the CANoe configuration and the message ID is contained in the database.

In order to send a SOME/IP message, the message must have a payload.

The created message can be deleted again with AREthReleaseMessage.

## Return Values

0: An error occurred. The error can be evaluated using the AREthGetLastError function.

## Example

```c
on key 's'
{
  dword messageId = 0x12340004; // service ID = 0x1234, method ID = 0x0004
  dword requestId = 0; // client ID = 0, session ID = 0
  dword protocolVersion = 1;
  dword interfaceVersion = 1;
  dword messageType = 0x2; // notification message
  dword returnCode = 0; // not available
  dword aep = 0;          // application endpoint handle
  dword messageHandle    = 0; // handle of the created SOME/IP message
  BYTE payload[5]; // the message payload
  dword count            = 0; // a simple counter

  // initialize the payload
  count = 0;
  payload[count++] = 0x11;
  payload[count++] = 0x22;
  payload[count++] = 0x33;
  payload[count++] = 0x44;
  payload[count++] = 0x55;

  // open application endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create the SOME/IP message itself and set the message payload
  messageHandle = AREthCreateMessage(messageId,requestId,protocolVersion,interfaceVersion,messageType,returnCode);
  AREthSetData(messageHandle,elcount(payload),payload);

  // send the SOME/IP message
  AREthOutputMessage(aep,0xFFFFFFFF,40001,messageHandle);

  // release the some IP message
  AREthReleaseMessage(messageHandle);
}
```

## Availability

| Since Version |
|---|
