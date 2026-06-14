# TCIL_SetTCStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetTCStatus(dword cycleTime); // form 1
```

## Description

This function changes the content and cycle time of the TC Status message.

Form 1 and 3: The content of TC Status message stays unchanged; only the cycle time is changed.

## Return Values

0: Function has been executed successfully

## Example

```c
pg PD pgPD;
pgPD.TCFunctionTCtoECU = 254;
pgPD.SourceAdressOfActiveWSM = 1;
pgPD.VisibleDataAlarmMaskID = 1000;
pgPD.VisibleSoftKeyMaskID = 2000;
pgPD.TCBusyCode1 = 0;
pgPD.TCBusyCode2 = 0;
pgPD.TCBusyCode3 = 0;
pgPD.TCBusyCode4 = 0;
pgPD.TCBusyCode8 = 0;
pgPD.TCFunctionCode = 0;
if (TCIL_SetTCStatus( TC, 1000, pgPD ) < 0)
{
  TestStepFail("Failed to set TC Status");
}
```

## Availability

| Since Version |
|---|
