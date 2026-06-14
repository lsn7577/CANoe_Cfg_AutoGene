# a429SetParity

> Category: `A429` | Type: `function`

## Syntax

```c
dword a429SetParity( a429word myA429word, int parity_value );
```

## Description

This function sets the selector parity of an ARINC word. So you may change the mode of parity generation for every single ARINC word.

Note: This modifies the ARINC word attributes only. For transmission call the function output.

## Availability

| Since Version |
|---|
