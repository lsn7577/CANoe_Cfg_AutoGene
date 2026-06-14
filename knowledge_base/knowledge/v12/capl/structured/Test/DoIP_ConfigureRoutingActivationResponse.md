# DoIP_ConfigureRoutingActivationResponse

> Category: `Test` | Type: `function`

## Syntax

```c
void DoIP_ConfigureRoutingActivationResponse(dword valueReserved);
```

## Description

Configures the routing activation response message sent by the vehicle simulation on the reception of a routing activation request message.

## Return Values

—

## Example

```c
// Set the reserved field in the routing activation response message to 0x12345678
DoIP_ConfigureRoutingActivationResponse(0x12345678);
```

## Availability

| Since Version |
|---|
