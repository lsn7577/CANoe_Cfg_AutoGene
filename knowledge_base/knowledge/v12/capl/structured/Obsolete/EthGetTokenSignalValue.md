# EthGetTokenSignalValue

> Category: `Obsolete` | Type: `function`

## Syntax

```c
double EthGetTokenSignalValue( long packet, dbSignal signal ); // form 1
```

## Description

Both functions assume that the packet’s payload is described in the database. They read the signal’s value of the packet’s payload.

Form 2 assumes the passed signal is the first element of an array. The value will be read from the element’s position.

The caller must check itself if the packet’s payload is described by the signal’s database frame.

## Return Values

Physical value

## Example

```c
on preStart
{
  EthReceivePacket( "OnEthPacket");
}
void OnEthPacket( LONG channel, LONG dir, LONG packet )
{
  DOUBLE coolantTemperature;

  if (EthGetTokenInt( packet, "udp", "destination" ) == 23) 
  //this example assumes that a udp payload with destination port 23 is described by the database frame EngineInfo
  {
    coolantTemperature = EthGetTokenSignalValue( packet, EngineInfo::CoolantTemperature );

    if (EthGetLastError() == 0)
    {
      write("CoolantTemperature is %f", coolantTemperature);
    }
  }
}
```

## Availability

| Up to Version |
|---|
