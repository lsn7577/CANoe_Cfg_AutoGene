# DoIP_SetTesterAdapter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetTesterAdapter(char adapter[]);
```

## Description

Sets the network interface to be used by the DoIP layer. This function must be called in on preStart.

## Return Values

—

## Example

```c
// Set the network adapter
char buffer[256];
DiagGetCommParameter( "DoIP.TESTER_Adapter", 0, buffer, elcount( buffer));
DoIP_SetTesterAdapter( buffer);
```

## Availability

| Since Version |
|---|
