# serviceProviderRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
serviceProviderRef * <var>
```

## Description

References a service provider endpoint.

## Example

```c
serviceProviderRef MirrorAdjustment svc1;
svc1 = MirrorAdjustment.providerSide[LeftMirror];
svc1.ProvideService();
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the provider endpoint | char[] | Read only |
| Path Full path of the provider endpoint (including namespaces) | char[] | Read only |
| ProviderIndex Index of the provider. Note that the index may change if providers are added or removed. | dword | Read only |
| Address Generalized address of the endpoint. Can be used with binding-specific API like Abstract_GetDisplayName to retrieve information. | AddressHandle | Read only |
| Abstract_GetDisplayName | ../Functions/CAPLfunctionAbstractGetDisplayName.htm |  |
