# mostSetRxBufferCtrl

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetRxBufferCtrl(long channel, long mode)
```

## Description

Disables or enables the Rx buffer for messages of the control channel.

In case the parameter mode is set to '0' or '1' the result is reported by means of the callback function OnMostStress().

Disabling the Rx buffer means that exactly one more message is accepted. Afterwards the buffer is no longer enabled, i.e. further messages are rejected with "RxBuffer full" (see status flags of Tx acknowledgment).

After the measurement start the receive buffer is always enabled.

VN2640: Disabling the Rx buffer means that up to four control messages will be accepted, before the buffer is disabled and low level retries on the bus are provoked.

OptoLyzerOL3150o: The stress network interface controller (NIC) must have its bypass opened (see mostSetStressNodeParameter ).Only messages addressed to the StressNIC will be blocked.

## Return Values

See error codes

## Availability

| Since Version |
|---|
