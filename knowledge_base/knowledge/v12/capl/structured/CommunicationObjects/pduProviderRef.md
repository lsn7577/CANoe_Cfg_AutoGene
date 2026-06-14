# pduProviderRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
pduProviderRef * <var>
```

## Description

References a PDU provider endpoint.

## Example

```c
pduProviderRef MirrorAdjustment.StatusPDU pdu1;
pdu1 = MirrorAdjustment.providerSide[LeftMirror].StatusPDU;
$pdu1.StatusSignal = newValue;
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the provided endpoint | char[] | Read only |
| Path Full path of the provided endpoint (including namespaces) | char[] | Read only |
| ProviderIndex Index of the provider. Note that the index may change if providers are added or removed. | dword | Read only |
| ServiceProvider Reference to the provider of the service containing the PDU. | serviceProviderRef * | Read only |
| <SignalName> Accesses the specified signal on the PDU. | <Data type of the signal> |  |
