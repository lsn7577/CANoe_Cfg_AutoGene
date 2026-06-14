# frGwBypassStatic

> Category: `FlexRay` | Type: `function`

## Syntax

```c
long frGwBypassStatic (long bypass, long channel, long slotId, long baseCycle, long cycleRepetition); // form 1
```

## Description

Activates/deactivates the automatic routing for the given slot. The function can be used during measurement.

Form 2 can only be used FlexRay with dual channel gateway (AB-AB-Gateway) mode, see FlexRay gateway.

## Return Values

0 = Error

## Example

```c
variables
{
  int gToggleBypassMode = 0;
  int gBypassActive = 1;
  const int gwOutChannel = 2;
}

on key 'a'
{
  toggleBypassMode = 1; // starts the synchronized switch of the bypass mode
}

on FrPDU msgchannel1.PDU_Speed
{
  //PDU PDU_Speed
  const long slotId          = 12;
  const long baseCycle       = 0;
  const long cycleRepetition = 4;
  frPDU msgchannel2.PDU_Speed gPDU_Speed = {msgChannel = 2, fr_channelMask = 1};
  if (gToggleBypassMode == 1) // execute once
  {
    if( gBypassActive == 1 ) // bypassing is active
    {
      frGwBypassStatic(0, gwOutChannel, slotId, baseCycle, cycleRepetition); // disable bypassing
      gBypassActive = 0;
    }
    else
    {
      frGwBypassStatic(1, gwOutChannel, slotId, baseCycle, cycleRepetition); // enable bypassing
      gBypassActive = 1;
    }
    gToggleBypassMode = 0;
  }
  if(gBypassActive == 0)
  {
    //initialize Tx PDU with RX Payload
    memcpy(gPDU_Speed.fr_Payload,this.fr_Payload,gPDU_Speed.fr_PDULength);
    // payload modification for channel 2
    gPDU_Speed.rpm = this.rpm / 2;
    frUpdatePDU(gPDU_Speed, 1, 1); //Transmitt PDU
  }
}
```

## Availability

| Since Version |
|---|
