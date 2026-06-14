# SomeIpSerializeMessage

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpSerializeMessage( dword messageHandle, dword bufferLength, CHAR buffer[] );
```

## Description

Serializes a SOME/IP message into a data buffer. Both the SOME/IP header and the payload are serialized.

If the configuration of the SOME/IP message is invalid (for example, incorrect value in length field or invalid content of payload), the message is not corrected when serialized. The message is passed unchanged.

## Return Values

Number of copied bytes.
In the Event of an error, the function returns the value 0. The SomeIpGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
on key 's'
{
  DWORD messageId = 0x12340004; // service ID = 0x1234, method ID = 0x0004
  DWORD requestId = 0;          // client ID = 0, session ID = 0
  DWORD protocolVersion = 1;
  DWORD interfaceVersion = 1;
  DWORD messageType = 0x2;      // notification message
  DWORD returnCode = 0;         // not available
  DWORD aep;                    // application endpoint handle
  DWORD messageHandle = 0;      // handle of the created SOME/IP message
  BYTE payload[5];              // the message payload
  DWORD count;                  // a simple counter
  BYTE buffer[21];             // serialization buffer

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

  // serialize message to data buffer
  SomeIpSerializeMessage(messageHandle,elcount(buffer),buffer);

  // The serialized message can now be added to a pure Ethernet frame using the function „EthSetTokenData“.
}
```

## Availability

| Since Version |
|---|
