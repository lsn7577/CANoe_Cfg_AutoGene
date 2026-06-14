# SomeIpSetReturnCode

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetReturnCode ( dword messageHandle, dword returnCode );
```

## Description

This function sets the return code in the SOME/IP message header.

## Parameters

| Name | Description |
|---|---|
| messageHandle | Handle of the SOME/IP message (e.g. see OnSomeIpMessage) |
| returnCode | 0x00: E_OK 0x01: E_NOT_OK 0x02: E_UNKNOWN_SERVICE 0x03: E_UNKNOWN_METHOD 0x04: E_NOT_READY 0x05: E_NOT_REACHABLE 0x06: E_TIMEOUT 0x07: E_WRONG_PROTOCOL_VERSION 0x08: E_WRONG_INTERFACE_VERSION 0x09: E_MALFORMED_MESSAGE 0x09: 0x1F RESERVED If message type is REQUEST, REQUEST_NO_RETURN or NOTIFICATION return code is N/A and set to 0x00 (E_OK). |

## Example

```c
on key 's'
{
  DWORD messageId        = 0x12340004; // service ID = 0x1234, method ID = 0x0004
  DWORD requestId        = 0;          // client ID = 0, session ID = 0
  DWORD protocolVersion  = 1;
  DWORD interfaceVersion = 1;
  DWORD messageType      = 0x2;        // notification message
  DWORD returnCode       = 0;          // not available
  DWORD aep              = 0;          // application endpoint handle
  DWORD messageHandle    = 0;          // handle of the created SOME/IP message
  BYTE payload[5];                     // the message payload
  DWORD count            = 0;          // a simple counter

  // initialize the payload
  count = 0;
  payload[count++] = 0x11;
  payload[count++] = 0x22;
  payload[count++] = 0x33;
  payload[count++] = 0x44;
  payload[count++] = 0x55;

  // open application endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // create the SOME/IP message itself and set the message payload
  messageHandle = SomeIpCreateMessage(messageId,requestId,protocolVersion,interfaceVersion,messageType,returnCode);
  SomeIpSetData(messageHandle,elcount(payload),payload);

  // send five SOME/IP message using different return codes
  for(count = 0; count < 5; count++)
  {
    SomeIpSetReturnCode(messageHandle,count);
    SomeIpOutputMessage(aep,0xFFFFFFFF,40001,messageHandle);
  } // for

  // release the some IP message
  SomeIpReleaseMessage(messageHandle);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
