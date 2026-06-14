# AREthPostMessage

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthPostMessage( dword aepHandle, dword remoteIPv4Address, dword remotePort, dword messageHandle ); // form 1
long AREthPostMessage( dword aepHandle, IP_Endpoint remoteIPEndpoint, dword messageHandle ); // form 2
```

## Description

This function is used to buffer a SOME/IP message.

All buffered messages are sent after the current CAPL function is exited. If the AREthPostMessage function is called multiple times in a CAPL function, the SOME/IP messages are collected and sent together (provided they have the same source and the same destination).

The call of AREthOutputMessage also triggers the sending of the buffered messages.

## Parameters

| Name | Description |
|---|---|
| aepHandle | Handle of the local Application Endpoint over which the message should be sent. |
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
  dword aep;                    // application endpoint handle
  dword messageHandle = 0; // handle of the created SOME/IP message
  BYTE payload[5]; // the message payload
  dword count; // a simple counter

  // initialize the payload
  count = 0;
  payload[count++] = 0x11;
  payload[count++] = 0x22;
  payload[count++] = 0x33;
  payload[count++] = 0x44;
  payload[count++] = 0x55;

  // open application endpoint
  aep = AREthOpenLocalApplicationEndpoint(17, 50002);

  // create the SOME/IP message itself
  messageHandle = AREthCreateMessage(messageId,requestId,protocolVersion,interfaceVersion,messageType,returnCode);

  // set message payload
  AREthSetData(messageHandle,elcount(payload),payload);

  // post two messages
  AREthPostMessage(aep,0xFFFFFFFF,40002,messageHandle);
  AREthPostMessage(aep,0xFFFFFFFF,40001,messageHandle);

  // if CAPL function is left, the two posted messages are send
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
