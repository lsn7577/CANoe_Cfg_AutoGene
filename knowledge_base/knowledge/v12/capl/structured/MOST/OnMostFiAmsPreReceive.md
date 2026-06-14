# OnMostFiAmsPreReceive

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostFiAmsPreReceive(mostAmsMessage * msg);
```

## Description

When fault injection is active, this function is called before the simulation node (CAPL program or node layer module) receives the AMS message. This allows incoming messages to be manipulated in order to emulate faulty application behavior.

The message can be suppressed (return value 0), forwarded (return value 1), or forwarded as an altered message (use of mostFiAmsReceive).

## Parameters

| Name | Description |
|---|---|
| msg | This variable contains the AMS message of the simulation node to be received. |

## Return Values

The return value can be used to control whether or not the message is to be received by the simulation node.
0: Original message is not received.1: Original message is received without alteration

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

| Since Version |
|---|
