# msgBeep

> Category: `Other` | Type: `function`

## Syntax

```c
void msgBeep (long soundType)
```

## Description

The msgBeep function plays back a sound predefined by the Windows system. It replaces the previous beep function.

## Parameters

| Name | Description |
|---|---|
| 0 | MB_ICONASTERISK SystemAsterisk |
| 1 | MB_ICONEXCLAMATION SystemExclamation |
| 2 | MB_ICONHAND SystemHand |
| 3 | MB_ICONQUESTION SystemQuestion |
| 4 | MB_OK SystemDefault |
| 5 | Standard beep using the PC speaker (default) |

## Return Values

—

## Example

```c
void sound() {
// Standard signal question
msgBeep (3);
}
```

## Availability

| Since Version |
|---|
