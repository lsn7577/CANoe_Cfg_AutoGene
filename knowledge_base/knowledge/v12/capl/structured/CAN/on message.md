# on message

> Category: `CAN` | Type: `event`

## Description

The event procedure on message is called on the receipt of a valid CAN message.

To access the control information you would use selectors.

The key word this is available within an on message procedure, to access the data of the message that has just been received.

CAPL programs are by default not transparent to bus events. This means that a CAPL node in the evaluation branch of the measurement configuration will block the data flow to its right side. You must explicitly program the passing of messages in CAPL nodes in the evaluation branch.

To make the CAPL node transparent to messages you would write:

However, please note that you are programming a recursive if you are using this code in CANoe's simulation configuration: For each message received, the reaction is to immediately resend the same message on the bus, causing the event procedure on message * to be called, etc.

If for example a CAPL program contains the on message procedures on message 123 and on message *, the procedure on message 123 will be called up, when a message with the identifier 123 is received. For all other messages the procedure on message * will be called up.

In contrast to bus events, value changes of environment variables are transparent to CAPL programs in the evaluation branch. Thus, a new environment variable is also available on the right side of CAPL nodes, and the user does not need to program this explicitly.

## Example

Gateway example

The gateway should transmit all messages between Bus 1 and Bus 2 in both directions:

Further examples

React to message 123 (dec, standard identifier), regardless of receiving chip

React to message 123 (dec, extended identifier), regardless of receiving chip

React to message 123 (hex, standard identifier), regardless of receiving chip

React to message 123 (hex, extended identifier), regardless of receiving chip

React to message EngineData

React to message 123 if it is received by CAN1 chip

Resolution of an Ambiguous Name

React to all messages, that are not used within another on message procedure in the same node.

React to all messages received by CAN2 chip (unboxed)

React to all messages received by CAN2 chip (boxed)

React to messages 0, 1 and 10 through 20

```c
on message CAN1.*
{
   message CAN2.* msg;
   if(this.dir != rx) return; //important!
   msg = this;
 output(msg);
}

on message CAN2.*
{
   message CAN1.* msg;
   if(this.dir != rx) return; //important!
   msg = this;
 output(msg);
}
on message 123
on message 123x
on message 0x123
on message 0x123x
on message EngineData
on message CAN1.123
on message CAN1.<symbolic name>
on message *
on message CAN2.*
on message CAN2.[*]
on message 0,1,10-20
```

## Availability

| Since Version |
|---|

## Selectors

| Message | ../CAPLfunctionMessageSelectors.htm |
|---|---|
