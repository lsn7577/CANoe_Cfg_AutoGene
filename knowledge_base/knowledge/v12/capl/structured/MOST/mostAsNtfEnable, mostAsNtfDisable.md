# mostAsNtfEnable, mostAsNtfDisable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfEnable()
```

## Description

mostAsNtfEnable() enables the notification service for the function block. The function block must be assigned to the CAPL program via mostApRegister(fblockID, instIDDefault) or the database.

mostAsNtfDisable() disables the notification service. The notification matrix is thereby deleted.

## Return Values

—

## Availability

| Since Version |
|---|
