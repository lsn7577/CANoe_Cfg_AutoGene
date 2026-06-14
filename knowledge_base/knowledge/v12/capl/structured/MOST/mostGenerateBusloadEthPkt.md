# mostGenerateBusloadEthPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateBusloadEthPkt(long channel, long pkts)
```

## Description

The function sends cyclical packets on the Ethernet channel. Use the mostConfigureBusloadEthPkt function to specify the send parameters and payload pattern.

## Return Values

See error codes

## Example

Configure and start bus load stress on keyboard event.

```c
on key 's'
{
   long i, channel, rate, countertype, counterpos, datalen;
   int64 srcadr, destadr;
   byte data[1506];

   channel     = 1;
   srcadr      = -1LL; // use own MAC address as source
   destadr     = 0x010203040506LL;
   rate        = 50;   // packets per second
   countertype = 4;    // 4 byte counter
   counterpos  = 9;    // counter in byte6..byte9
   datalen     =300;

   // fill payload of stress packet
   for(i = 0; i < datalen; ++i)
      data[i] = (byte)i;

   // configure stress pattern
   mostConfigureBusloadEthPkt(channel, rate, countertype, counterpos, srcadr, destadr, datalen, data);

   // start generation of 500 packets
   mostGenerateBusloadEthPkt(channel, 500);
}
```

## Availability

| Since Version |
|---|
