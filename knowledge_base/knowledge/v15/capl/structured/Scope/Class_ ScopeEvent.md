# Class: ScopeEvent

> Category: `Scope` | Type: `notes`

## Description

—

Occurs when the Connect Scope action initiated with the scopeConnect() CAPL call is successfully completed.

Occurs when the Disconnect Scope action initiated with the scopeDisconnect() CAPL call is successfully completed.

testGetWaitScopeEventData | testWaitForScopeEvent

| Keyword | Description | Type | Access Limitations |
|---|---|---|---|
| Type | Type of scope event. | enum ScopeEventType | Read-only |
| DataID | Data identifier of the captured data created after re-quest to trigger on Scope hardware completed. | int | Read-only |
| Time | Time stamp of the captured data created after request to trigger on Scope hardware completed. | int64 | Read-only |

| Value | Description |
|---|---|
| scopeConnected | Occurs when the Connect Scope action initiated with the scopeConnect() CAPL call is successfully completed. |
| scopeDisconnected | Occurs when the Disconnect Scope action initiated with the scopeDisconnect() CAPL call is successfully completed. |
| scopeTriggerActivated | Occurs when the Scope trigger activation initiated with the scopeActivateTrigger() CAPL call is successfully completed. |
| scopeTriggerDeactivated | Occurs when the Scope trigger deactivation initiated with the scopeDeactivateTrigger() CAPL call is successfully completed. |
| scopeTriggered | Occurs when the Scope triggering action initiated with the scopeTriggerNow() CAPL call is successfully completed. |

| Version 15© Vector Informatik GmbH |
|---|
