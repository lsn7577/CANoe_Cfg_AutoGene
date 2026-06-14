# TCIL_SetResponseContent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetResponseContent(dbNode client, dword command, dword subcommand, pg pgPD); // form 1
```

## Description

The function changes the content of the next TC response TC12 sent by the TC IL to allow fault injection.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
pg PD pgPD;
InitJ1939PGData(pgPD);
pdgPD.Command = 1; // Subcommand for the transfer and management of device descriptors
pgPD.DeviceDescriptionMsgType = 5; // Request Object Pool Transfer response
pgPD.Status                   = 1; // Not enough memory available
result = TCIL_SetResponseContent(TC, Sprayer, 1, 5, pgPD);
if (result < 0)
{
  TestStepFail("Failed to modify Request Object Pool response");
}
```

## Availability

| Since Version |
|---|
