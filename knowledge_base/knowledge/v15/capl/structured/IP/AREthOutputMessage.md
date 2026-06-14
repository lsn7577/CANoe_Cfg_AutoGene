# AREthOutputMessage

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthOutputMessage( dword aepHandle, dword remoteIPv4Address, dword remotePort, dword messageHandle ); // form 1
long AREthOutputMessage( dword aepHandle, IP_Endpoint remoteIPEndpoint, dword messageHandle); // form 2
```

## Description

This function is used to send a SOME/IP message.

The packet is sent immediately. All messages that were prepared for sending beforehand with AREthPostMessage are inserted in the packet to be sent and sent with the message, provided that the buffered messages have the same source and the same destination.

## Parameters

| Name | Description |
|---|---|
| aepHandle | Handle of the local Application Endpoint over which the message should be output. |
| remoteIPv4Address | IPv4 address to which the message should be sent (Network Byte Order). |
| remotePort | UDP/TCP port number to which the message should be sent. |
| remoteIPEndpoint | Object of type IP_Endpoint that contains the address/port of the remote endpoint. |
| messageHandle | Handle of the message that was created with AREthCreateMessage, for example. |

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
  dword aep = 0; // application endpoint handle
  dword messageHandle = 0; // handle of the created SOME/IP message
  BYTE payload[5]; // the message payload
  dword count = 0; // a simple counter

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2: form 1 12.0 SP2: form 2 | — | — | — | 2.1 SP3: form 1 4.0 SP2: form 2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
