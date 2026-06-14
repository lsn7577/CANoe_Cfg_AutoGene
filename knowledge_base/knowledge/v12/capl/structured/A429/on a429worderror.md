# on a429worderror

> Category: `A429` | Type: `event`

## Description

The event procedure on a429worderror is called on every event, related to an ARINC word error. The error type is available in the selector error.

Note that there are errors without any valid label information. This is especially the gap violation error. The ARINC word causing that error triggers a on a429word procedure. For this reason it makes sense to catch all errors in a single channel related handler.

ARINC word errors are also monitored with statistics system variables.

## Availability

| Since Version |
|---|

## Selectors

| a429word | ../CAPLfunctionsA429DefineARINCword.htm |
|---|---|
