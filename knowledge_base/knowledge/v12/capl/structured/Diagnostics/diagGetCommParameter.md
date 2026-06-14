# diagGetCommParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetCommParameter (char paramName[]); // form 1
```

## Description

Returns the value of a numeric/textual communication parameter of the given or currently active diagnostic description. The values are read from the diagnostic description if they cannot be set in the configuration dialog.

## Parameters

| Name | Type | Description |
|---|---|---|
| Qualifier | Available in | Description |
| CANoe.AddressMode |  | ISO TP address mode: 0: Normal 1: Extended 2: NormalFixed 3: Mixed <0: No ISO TP |
| CANoe.TxId | [0 1*] | CAN Id for transmitted frames |
| CANoe.RxId | [0 1*] | CAN Id for received frames |
| CANoe.BaseAddress | [1*] | TP base address |
| CANoe.EcuAddr | [1 2 3] | Number of this node |
| CANoe.TgtAddr | [1 2 3] | Target node number |
| CANoe.AddrExt | [3] | Address extension byte |
| CANoe.TxPrio | [2 3] | Frame transmit priority |

## Return Values

Error code or value of the parameter.

## Example

For details and an example please refer to the reference implementation of the K-Line CAPL Callback Interface for diagnostics that is installed under

and can be included in CAPL programs with

```c
#include "Diagnostics\CCI_KLine.cin"
```

## Availability

| Since Version |
|---|
