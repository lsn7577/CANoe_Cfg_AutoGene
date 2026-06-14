# OnSomeIpProcessRxMessage

> Category: `IP` | Type: `function`

## Syntax

```c
long OnSomeIpProcessRxMessage(dword messageHandle, long rxChannel);
```

## Description

This callback function is called whenever the IL has received a SOME/IP message.

The return value of this callback determines if the message should be processed by the IL or if it should be ignored. Furthermore the message may be modified before the IL processes the message.

## Parameters

| Name | Description |
|---|---|
| messageHandle | Handle of the received SOME/IP message that triggered the callback. |
| rxChannel | The channel of the application endpoint that received the message. |

## Return Values

The message will be processed if the callback returns 1.Otherwise the message has been ignored by the callback.

## Example

```c
long OnSomeIpProcessRxMessage(dword messageHandle, long rxChannel)
{
  DWORD msgId = 0;
  LONG errorCode = 0;
  LONG errorOccured = 0;
  // get data from SOME/IP message
  if((msgId = SomeIpGetMessageId(messageHandle)) == 0)
  {
    // check if last function was executed correct
    if((errorCode = SomeIpGetLastError()) != 0)
    {
      write("SOME/IP IL error occured: Error code: %d", errorCode);
      errorOccured = 1;
    } // if
  } // if
  if(errorOccured == 0)
  {
    write("SOME/IP message with Message ID 0x%08x received",msgId);
    return 1;
  } // if
  else
  {
    return 0;
  } // else
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
