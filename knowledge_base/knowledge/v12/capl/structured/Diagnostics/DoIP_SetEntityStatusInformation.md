# DoIP_SetEntityStatusInformation

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetEntityStatusInformation(long nodeType, dword maxRequestSize);
```

## Description

Configures the response sent for an entity status request.

## Return Values

—

## Example

```c
// The ECU simulation will return type "node" and a maximum length supported
// by this protocol implementation
DoIP_SetEntityStatusInformation( 1, 0xFFFFFFFF);
```

## Availability

| Since Version |
|---|
