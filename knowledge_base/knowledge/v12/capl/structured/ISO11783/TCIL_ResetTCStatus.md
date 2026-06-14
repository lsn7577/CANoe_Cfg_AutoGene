# TCIL_ResetTCStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ResetTCStatus( ); // form 1
```

## Description

This function reverts changes made by TCIL_SetTCStatus and turns back to the default behavior of the Task Controller IL.

## Return Values

0: Function has been executed successfully

## Example

```c
pg TC12 tc12;
tc12.TCFunctionTCtoECU = 254;
tc12.SourceAdressOfActiveWSM = 1;
tc12.VisibleDataAlarmMaskID = 1000;
tc12.VisibleSoftKeyMaskID = 2000;
tc12.TCBusyCode1 = 0;
tc12.TCBusyCode2 = 0;
tc12.TCBusyCode3 = 0;
tc12.TCBusyCode4 = 0;
tc12.TCBusyCode8 = 0;
tc12.TCFunctionCode = 0;
if (TCIL_SetTCStatus( TC, 1000, tc12 ) < 0)
{
  TestStepFail("Failed to set TC Status");
}
```

## Availability

| Since Version |
|---|
