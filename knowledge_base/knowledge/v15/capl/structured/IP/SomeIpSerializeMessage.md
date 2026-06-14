# SomeIpSerializeMessage

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpSerializeMessage( dword messageHandle, dword bufferLength, CHAR buffer[] );
dword SomeIpSerializeMessage( dword messageHandle, dword bufferLength, BYTE buffer[] );
dword SomeIpSerializeMessage( dword messageHandle, dword bufferLength, struct buffer[] );
```

## Description

Serializes a SOME/IP message into a data buffer. Both the SOME/IP header and the payload are serialized.

## Parameters

| Name | Description |
|---|---|
| messageHandle | Handle of the message that was created with SomeIpCreateMessage, for example. |
| bufferLength | Length of the buffer parameter in bytes. |
| buffer | Data buffer into which the SOME/IP message is serialized. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP2 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
