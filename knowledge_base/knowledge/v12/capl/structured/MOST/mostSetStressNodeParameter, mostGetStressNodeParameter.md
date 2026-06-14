# mostSetStressNodeParameter, mostGetStressNodeParameter

> Category: `MOST` | Type: `function`

## Syntax

```c
mostSetStressNodeParameter(1, 1, 0x123);
mostSetStressNodeParameter(1, 3, 0);
```

## Description

VN2640:

Additional parameters of the stress generators (mostGenerateBusloadCtrl, mostGenerateBusloadAsync, mostGenerateBusloadEthPkt) can be set with mostSetStressNodeParameter.

OptoLyzer G2 3150o,OptoLyzer MOCCA compact 50e and OptoLyzer MOCCA compact 150c:

The interfaces for MOST150 provides stress functionality through an additional network interface controller (NIC). For a set of stress functions (mostSetRxBufferCtrl, mostSyncAlloc) the NIC is required to be visible in the network (bypass open).

With mostSetStressNodeParameter the MOST node parameters of this additional NIC can be configured.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |

## Return Values

mostSetStressNodeParameter: See error codes

## Example

```c
// configure stress controller as visible network node with logical address 0x123
mostSetStressNodeParameter(1, 1, 0x123); // set node address
mostSetStressNodeParameter(1, 3, 0); // open bypass
```

## Availability

| Since Version |
|---|
