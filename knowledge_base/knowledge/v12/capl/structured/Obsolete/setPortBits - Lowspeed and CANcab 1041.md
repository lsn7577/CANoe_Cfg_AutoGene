# setPortBits - Lowspeed and CANcab 1041

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void setPortBits (byte Mode);
```

## Description

To enable the different CAN bus tranceiver modes Normal Mode (standard at start) or Sleep Mode.

For this function you have to take care that the channel number is the logical one which is used by CANalyzer / CANoe according to the assignment in CAN Driver Configuration.

## Parameters

| Name | Description |
|---|---|
| Bit 0 and 1 | Linemode of channel 1 CANcabs |
| Bit 2 and 3 | Linemode of channel 2 CANcabs |
| Bit 4 – 7 | Reserved and must be set to "0" |

## Return Values

—

## Example

Changing the mode of two lowspeed CANcabs:

```c
variables {
}
on key '1'
{
write ("CAN1 Lowspeed: Normal Mode");
setPortBits (0x01);
}
on key '2'
{
write ("CAN1 Lowspeed: Sleep Mode");
setPortBits (0x02);
}
on key '3'
{
write ("CAN2 Lowspeed: Normal Mode");
setPortBits (0x04);
}
on key '4'
{
write ("CAN2 Lowspeed: Sleep Mode");
setPortBits (0x08);
}
```

## Availability

| Up to Version |
|---|
