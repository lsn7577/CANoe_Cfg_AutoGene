# setPortBits - Single Wire

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void setPortBits (byte Mode);
```

## Description

To enable the different CAN bus transceiver modes.

For this function you have to take care that the channel number is the logical one which is used by CANalyzer / CANoe according to the assignment in CAN Driver Configuration. Further on, setting the mode explicitly for one channel is not possible, you always have to set the modes for both channels (which can be different modes of course).

## Parameters

| Name | Description |
|---|---|
| Bit 0 and 1 | Linemode of CANcab on channel 1 |
| Bit 2 and 3 | Linemode of CANcab on channel 2 |
| Bit 4 | High priority for channel 1 |
| Bit 5 | High priority for channel 2 |
| Bits 6 and 7 | Reserved, must be set to "0" |

## Return Values

—

## Example

Sending a HighVoltage-WakeUp message on logical CAN channel 1:

```c
variables {
message 0x100 msg;
}
on start
{
msg.CAN = 1;
msg.DLC = 0;
}
on key 'w' 
{
// sets the transceiver of channel 1 in HighVoltage mode 
// and the transceiver of channel 2 in Normal mode.
setPortBits(0x0D);
// sends the message.
output(msg);
 
// After sending the Wakeup message the transceiver
// of both channels will be set to Normal mode.
setPortBits(0x0F);
}
on message *
{
output(this);
}
```

## Availability

| Up to Version |
|---|
