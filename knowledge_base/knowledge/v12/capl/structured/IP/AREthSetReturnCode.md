# AREthSetReturnCode

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSetReturnCode ( dword messageHandle, dword returnCode );
```

## Description

This function sets the return code in the SOME/IP message header.

## Example

```c
on key 's'
{
  dword messageId        = 0x12340004; // service ID = 0x1234, method ID = 0x0004
  dword requestId        = 0;          // client ID = 0, session ID = 0
  dword protocolVersion  = 1;
  dword interfaceVersion = 1;
  dword messageType      = 0x2;        // notification message
  dword returnCode       = 0;          // not available
  dword aep              = 0;          // application endpoint handle
  dword messageHandle    = 0;          // handle of the created SOME/IP message
  BYTE payload[5];                     // the message payload
  dword count            = 0;          // a simple counter

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

  // send five SOME/IP message using different return codes
  for(count = 0; count < 5; count++)
  {
    AREthSetReturnCode(messageHandle,count);
    AREthOutputMessage(aep,0xFFFFFFFF,40001,messageHandle);
  } // for

  // release the some IP message
  AREthReleaseMessage(messageHandle);
}
```

## Availability

| Since Version |
|---|
