# TestWaitForTimeout

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForTimeout(dword aTimeout);
```

## Description

Waits until the expiration of the specified timeout time.

## Return Values

-2: Resume due to constraint violation

## Example

```c
// waits for 3000 ms
long result;
result = TestWaitForTimeout(3000);
```

## Availability

| Since Version |
|---|
