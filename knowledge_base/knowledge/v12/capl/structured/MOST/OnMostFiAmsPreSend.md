# OnMostFiAmsPreSend

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostFiAmsPreSend(mostAmsMessage * msg);
```

## Parameters

| Name | Description |
|---|---|
| msg | This variable contains the send request of the simulation node. |

## Return Values

The return value can be used to control whether or not the message is sent.
0: Original message is not sent1: Original message is sent without alteration

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

| Since Version |
|---|
