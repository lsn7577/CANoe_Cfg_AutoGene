# diagGetCommParameter (FlexRay)

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetCommParameter (char qualifier[]);
```

## Description

Returns the value of a numeric/textual communication parameter of the given or currently active diagnostic description. The values are read from the diagnostic description if they cannot be set in the configuration dialog.

## Parameters

| Name | Description |
|---|---|
| Qualifier | Description |
| FlexRay.Protocol | The protocol variant to use. 0 AUTOSAR 2.xrest reserved for future extensions |
| Values |  |
| 1 | One byte addresses |
| 2 | Two byte addresses |
| FlexRay.LocalAddress | Address of *this* node, i.e. ECU address in ECU simulation, tester address in tester nodes. |
| FlexRay.RemoteAddress | Address of the target node, i.e. ECU address in tester nodes, tester address in ECU simulation. |
| Values |  |
| 1 | Unicast |
| 2 | Acknowledged Unicast |
| 3 | Acknowledged Unicast with Retry |
| rest | reserved |
| Note Please refer to the AUTOSAR FlexRay TP specification for details on the parameter value semantics. |  |
| Values |  |
| 1 | ISO |
| 2 | ISO6 |
| 3 | L16M |
| 4 | L4G |
| rest | reserved |
| Note Please refer to the AUTOSAR FlexRay TP specification for details on the parameter value semantics. |  |
| Note Please refer to the AUTOSAR FlexRay TP specification for details on the parameter value semantics. |  |
| Note Please refer to the AUTOSAR FlexRay TP specification for details on the parameter value semantics. |  |

## Return Values

Error code

## Availability

| Since Version |
|---|
