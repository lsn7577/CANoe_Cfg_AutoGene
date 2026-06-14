# linUpdateResponse

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linUpdateResponse(dword frameId, dword dlc, byte[] responseData); // form 1
```

## Description

Updates the response data of a specific LIN frame.

## Return Values

Returns 1 if the response update succeeded, otherwise 0.

## Example

```c
// Update the response of the LIN frame with the id 0x04

on linFrame 0x04

{
  long i;
  byte frm4data[8];

  for(i = 0; i < linGetDlc(this.id); i++)
  {
    frm4data[i] = this.byte(i) + 1;
  }

linUpdateResponse(this.id, linGetDlc(this.id), frm4data);
}
```

## Availability

| Since Version |
|---|
