# outputMostPktThis

> Category: `MOST` | Type: `function`

## Syntax

```c
outputMostPktThis()
```

## Description

Passes the packet on to the next node in the nodal sequence.

## Return Values

—

## Example

Packet filter in CAPL:

```c
OnMostPkt(long pktdatalen)
{
   // 
 filter destination address 0x100
   if(mostPktDestAdr() 
 == 0x100)
   {
      // 
 forward packet to the successor
      outputMostPktThis(); 
  
   }
}
```

## Availability

| Since Version |
|---|
