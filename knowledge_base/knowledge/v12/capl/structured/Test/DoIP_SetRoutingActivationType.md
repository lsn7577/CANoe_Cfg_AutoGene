# DoIP_SetRoutingActivationType

> Category: `Test` | Type: `function`

## Syntax

```c
long DoIP_SetRoutingActivationType(char ecuQualifier[], dword activationType);
```

## Description

Configures the value of the ISO 13400-2 parameter routing activation request activation type sent by the tester the next time it starts to communicate with a vehicle on the built-in channel. If no ECU qualifier is given, the channel selected with DiagSetTarget is used.

## Return Values

Error Code

## Example

```c
  // Try to connect to vehicle, changing activation type on failure
  testcase TryRoutingType()
  {
  diagRequest ECU.DefaultSession_Start req;
  long status;

  // Try the default routing activation type first
  DoIP_SetRoutingActivationType("ECU", 0);

  req.SendRequest();
  status = testWaitForDiagRequestSent(req, 2900);
  switch(status)
  {
    case 1:
      TestStepPass("Connect worked with default activation type");
      return;
    case 0:
      TestStepFail("Timeout trying to connect! No vehicle?");
      return;
    case -92:
      TestStep("", "Error on TP level, probably wrong activation type?");
      break;
    default:
      TestStepWarning( "", "Connecting with default activation type returned %d", status);
  }

  // Try again with arbitrary "OEM-specific" activation type
  DoIP_SetRoutingActivationType("ECU", 0xF0);

  req.SendRequest();
  status = testWaitForDiagRequestSent(req, 2900);
  if (status == 1)
    TestStepPass("Successfully connected with OEM-specific activation type");
  else if(status == 0)
    TestStepFail("Timeout trying to connect!");
  else
    TestStepFail( "", "Connecting with OEM-specific activation type returned %d", status);
}
```

## Availability

| Since Version |
|---|
