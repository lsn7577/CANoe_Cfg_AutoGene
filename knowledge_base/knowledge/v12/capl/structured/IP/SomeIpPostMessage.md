# SomeIpPostMessage

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpPostMessage( dword aepHandle, dword remoteIPv4Address, dword remotePort, dword messageHandle );
```

## Description

This function is used to buffer a SOME/IP message.

All buffered messages are sent after the current CAPL function is exited. If the SomeIpPostMessage function is called multiple times in a CAPL function, the SOME/IP messages are collected and sent together (provided they have the same source and the same destination).

The call of SomeIpOutputMessage also triggers the sending of the buffered messages.

## Return Values

0: The function was successfully executed

## Example

```c
on key 's'
{
  DWORD messageId = 0x12340004; // service ID = 0x1234, method ID = 0x0004
  DWORD requestId = 0; // client ID = 0, session ID = 0
  DWORD protocolVersion = 1;
  DWORD interfaceVersion = 1;
  DWORD messageType = 0x2; // notification message
  DWORD returnCode = 0; // not available
  DWORD aep;                    // application endpoint handle
  DWORD messageHandle = 0; // handle of the created SOME/IP message
  BYTE payload[5]; // the message payload
  DWORD count; // a simple counter

  // initialize the payload
  count = 0;
  payload[count++] = 0x11;
  payload[count++] = 0x22;
  payload[count++] = 0x33;
  payload[count++] = 0x44;
  payload[count++] = 0x55;

  // open application endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create the SOME/IP message itself
  messageHandle = SomeIpCreateMessage(messageId,requestId,protocolVersion,interfaceVersion,messageType,returnCode);

  // set message payload
  SomeIpSetData(messageHandle,elcount(payload),payload);

  // post two messages
  SomeIpPostMessage(aep,0xFFFFFFFF,40002,messageHandle);
  SomeIpPostMessage(aep,0xFFFFFFFF,40001,messageHandle);

  // if CAPL function is left, the two posted messages are send
}
```

## Availability

| Since Version |
|---|
