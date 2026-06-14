# <OnEthAdapterStatus>

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void <OnEthAdapterStatus>( long channel, long status);
```

## Description

This callback function is called when the state of the Ethernet adapter has changed.

## Return Values

—

## Example

```c
OnEthAdapterStatus( LONG channel, LONG status)
{
  switch(status)
  {
  case 1:   // adapter disconnected
    write("ETH%d disconnected", channel );
    break;
  case 2:   // adapter connected
    write("ETH%d connected", channel );
    break;
  default:
    break;
  }
}
```

## Availability

| Up to Version |
|---|
