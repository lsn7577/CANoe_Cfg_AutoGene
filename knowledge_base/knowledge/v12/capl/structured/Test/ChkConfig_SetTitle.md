# ChkConfig_SetTitle

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_SetTitle (dword aCheckId, char aTitle[]);
check.SetTitle(char aTitle[]);
```

## Description

Sets the title of a check.

The check is displayed in the Write Window and the test report with this title.

## Return Values

0: Title is set successfully

## Example

```c
// set title of the check
dword mCheckId;
mCheckId = ChkCreate_Timeout(1000);
ChkConfig_SetTitle(mCheckId, "Check Timeout");
ChkControl_Start(mCheckId);
TestCheck tc;
tc = TestCheck::CreateTimeout(1000);
tc.SetTitle("Check Timeout");
tc.Start();
```

## Availability

| Since Version |
|---|
