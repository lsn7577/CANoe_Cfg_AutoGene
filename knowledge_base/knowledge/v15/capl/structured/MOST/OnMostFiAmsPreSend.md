# OnMostFiAmsPreSend

> Category: `MOST` | Type: `function`

## Syntax

```c
long OnMostFiAmsPreSend(mostAmsMessage * msg);
```

## Parameters

| Name | Description |
|---|---|
| msg | This variable contains the send request of the simulation node. The number of transmitted data can be up to 65535 bytes for a mostAmsMessage. For reasons of efficiency, only the first 200 bytes are copied to the msg variable. To facilitate access to the entire message's user data, the message can be assigned to an AMS message declared with a sufficient size (see example below). |

## Return Values

The return value can be used to control whether or not the message is sent.
0: Original message is not sent
1: Original message is sent without alteration

## Example

```c
// change all Status messages a simulated node tries to send to error messages
long OnMostFiAmsPreSend(mostAmsMessage * msg)
{
   if(msg.OpType == 0xC) // Status or Result message
   {
      // make a copy
      mostAmsMessage * modMsg = {DLC = 1000}; // buffer for 1000 data bytes
      modMsg = msg; // at most 1000 data bytes are copied here

      // modify OpType
      modMsg.OpType = 0xF;
      // keep message length and data
      // but change the first byte
      modMsg.byte(0) = 0x0B; // set ErrorCode=Device malfunction
      // send modified message
      output(modMsg);

      // do not send original message
      return 0;
   }
   else
   {
      // send original message
      return 1;
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
