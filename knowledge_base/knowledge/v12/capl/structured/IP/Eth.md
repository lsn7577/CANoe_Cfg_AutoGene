# Eth

> Category: `IP` | Type: `function`

## Syntax

```c
Eth <Ethernet Channel Number>;
```

## Description

Can be used to get the status and statistics of the Ethernet link.

Use ethResetStatistics to reset the statistics values.

## Example

```c
switch(Eth1.status)
{
  case 0:
    write("Ethernet link on Eth1 is down” );
    break;
  case 1:
    write("Ethernet link on Eth1 is up with %dMBit/sec“, Eth1.bitrate/1000);
}
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| status 0 – Link down 1 – Link up | long | Read only |
| bitrate Bit rate in kBit/sec | dword | Read only |
| TxBitrate Current TX bitrate in [kBit/sec] | dword | Read only |
| RxBitrate Current TX bitrate in [kBit/sec] | dword | Read only |
| TxPacketRate Current TX packet rate [pkt/sec] | dword | Read only |
| RxPacketRate Current TX packet rate [pkt/sec] | dword | Read only |
| TxPacketCount Number of transmitted Ethernet packets | qword | Read only |
| RxPacketCount Number of received Ethernet packets | qword | Read only |
| TxByteCount Number of transmitted bytes | qword | Read only |
| RxByteCount Number of received bytes | qword | Read only |
| TxErrorCount Number of transmitted error packets | dword | Read only |
| RxErrorCount Number of received error packets | dword | Read only |
| SQI Current Service Quality Indicator: 0 – Error Occurring 1 – No Margin 2 – Marginal 3 – Acceptable 4 – Good 5 – Excellent 6 - not available | dword | Read only |
