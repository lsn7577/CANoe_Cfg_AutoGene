# on message

> Category: `CAN` | Type: `event`

## Description

The event procedure on message is called on the receipt of a valid CAN message.

To access the control information you would use selectors.

The key word this is available within an on message procedure, to access the data of the message that has just been received.

CAPL programs are by default not transparent to bus events. This means that a CAPL node in the evaluation branch of the measurement configuration will block the data flow to its right side. You must explicitly program the passing of messages in CAPL nodes in the evaluation branch.

To make the CAPL node transparent to messages you would write:

on message * { output(this);};

However, please note that you are programming a recursive if you are using this code in CANoe's simulation configuration: For each message received, the reaction is to immediately resend the same message on the bus, causing the event procedure on message * to be called, etc.

## Example

Gateway Example

The gateway should transmit all messages between Bus 1 and Bus 2 in both directions:

Further Examples

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |

## Selectors

| Message | ../CAPLfunctionMessageSelectors.htm |
|---|---|
