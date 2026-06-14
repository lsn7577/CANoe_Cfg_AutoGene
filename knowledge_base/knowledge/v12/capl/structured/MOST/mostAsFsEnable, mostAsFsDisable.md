# mostAsFsEnable, mostAsFsDisable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsFsEnable()
```

## Description

mostAsFsEnable() makes the function service available for the function block. The function block must be assigned to the CAPL program via mostApRegister(fblockID, instIDDefault) or the database. Furthermore mostAsFsEnable() enables the functions <FktIDs>, <Notification> and <NotificationCheck> of the function block for the notification service.

mostAsFsDisable() disables the function service.

## Return Values

See error codes

## Availability

| Since Version |
|---|
