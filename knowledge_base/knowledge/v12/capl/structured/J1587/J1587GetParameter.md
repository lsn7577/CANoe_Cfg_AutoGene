# J1587GetParameter

> Category: `J1587` | Type: `function`

## Syntax

```c
byte J1587GetParameter(J1587Message msg /*in*/, J1587Param param /*out*/, word index /*in*/)
```

## Description

Gets a J1587 parameter inside a J1708 message at a given index.

## Return Values

0 or error code

## Example

```c
on J1587Message 50 // 50 is Sender MID, can be dbNode name or MID
{
  dword count, i;
  J1587Param param;
  count = GetParameterCount(this);

  for (i = 0; i < count; i++) 
  {
    if (J1587GetParameter(this, param, i) == 0) 
    {
      write ("Parameter with PID %d received: %d", param.J1587_PID);
    }
  }
}
```

## Availability

| Since Version |
|---|
