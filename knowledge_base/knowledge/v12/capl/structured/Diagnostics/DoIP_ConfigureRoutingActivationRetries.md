# DoIP_ConfigureRoutingActivationRetries

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_ConfigureRoutingActivationRetries(dword numberOfRetries, dword retryPeriod_ms, byte nackCodes[], dword nackCodesCount);
```

## Description

Allows to activate or deactivate DoIP routing activation retries. Retries are only attempted for specific negative ACK codes that can be given in a list of codes. There is a default list that is used when nackCodesCount is 0.

## Return Values

—

## Example

```c
ActivateRetries()
{
  byte nackCodes[1];
  // Perform up to 3 retries when the default codes 0x04 or 0x11 are returned
  DoIP_ConfigureRoutingActivationRetries(3, 100, nackCodes, 0);
}

DeactivateRetries()
{
  byte nackCodes[1];
  // Turn off retries
  DoIP_ConfigureRoutingActivationRetries(0, 0, nackCodes, 0);
}
```

## Availability

| Since Version |
|---|
