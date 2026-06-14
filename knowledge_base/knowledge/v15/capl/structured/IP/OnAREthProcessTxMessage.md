# OnAREthProcessTxMessage

> Category: `IP` | Type: `function`

## Syntax

```c
long OnAREthProcessTxMessage(dword messageHandle, long txChannel);
```

## Description

This callback function is called whenever the IL wants to send a SOME/IP message.

The return value of this callback determines if the message should be send or if it should be blocked. Furthermore the message may be modified before the IL sends the message.

## Parameters

| Name | Description |
|---|---|
| messageHandle | Handle of the to be sent message that triggered the callback. |
| txChannel | The channel of the application endpoint that will be used to send the message. |

## Return Values

The message will be send if the callback returns 1.
Otherwise the message has been filtered by the callback.

## Example

```c
long OnAREthProcessTxMessage(dword messageHandle, long txChannel)
{
  DWORD msgId = 0;
  LONG errorCode = 0;
  LONG errorOccured = 0;
  // get data from SOME/IP message
  if((msgId = AREthGetMessageId(messageHandle)) == 0)
  {
    // check if last function was executed correct
    if((errorCode = AREthGetLastError()) != 0)
    {
      write("SOME/IP IL error occured: Error code: %d", errorCode);
      errorOccured = 1;
    } // if
  } // if
  if(errorOccured == 0)
  {
    write("SOME/IP message with Message ID 0x%08x is send",msgId);
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
| Since Version | — | 9.0 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
