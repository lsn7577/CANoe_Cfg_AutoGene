# mostGenerateBusloadEthPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateBusloadEthPkt(long channel, long pkts);
```

## Description

The function sends cyclical packets on the Ethernet channel. Use the mostConfigureBusloadEthPkt function to specify the send parameters and payload pattern.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| 0 | Stops the busload generation |
| >0 | Sends the given number of packets |
| -1 | Sends continual packets |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 7.5 SP2 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
