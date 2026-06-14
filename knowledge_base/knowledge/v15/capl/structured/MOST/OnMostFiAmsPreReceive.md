# OnMostFiAmsPreReceive

> Category: `MOST` | Type: `function`

## Syntax

```c
long OnMostFiAmsPreReceive(mostAmsMessage * msg);
```

## Description

When fault injection is active, this function is called before the simulation node (CAPL program or node layer module) receives the AMS message. This allows incoming messages to be manipulated in order to emulate faulty application behavior.

The message can be suppressed (return value 0), forwarded (return value 1), or forwarded as an altered message (use of mostFiAmsReceive).

## Parameters

| Name | Description |
|---|---|
| msg | This variable contains the AMS message of the simulation node to be received. The number of transmitted data can be up to 65535 bytes for a mostAmsMessage. For reasons of efficiency, only the first 200 bytes are copied to the msg variable. To facilitate access to all the message's user data, the message can be assigned to an AMS message declared with a sufficient size (see example below). |

## Return Values

The return value can be used to control whether or not the message is to be received by the simulation node.
0: Original message is not received.
1: Original message is received without alteration

## Example

```c
// change all Set operations to SetGet operations
// before the simulation node receives the message
long OnMostFiAmsPreReceive(mostAmsMessage * msg)
{
   // The following if statement prevents this code from being called recursively
   // e.g. by ignoring the Tx acknowledgments
   if((msg.OpType == 0x0) && (msg.dir == Rx)) // Set message
   {
      // make a copy
      mostAmsMessage * modMsg = {DLC = 1000}; // buffer for 1000 data bytes
      modMsg = msg; // at most 1000 data bytes are copied here

      // modify OpType
      modMsg.OpType = 0x2;
      // forward modified message to simulation node
      mostFiAmsReceive(modMsg);

      // do not forward the original message
      return 0;
   }
   else
   {
      // forward the original message
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
