# AvbSetCrfAudioSampleClockMultiplier

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Set property TimestampRate on the media type (retrievable via AvbGetMediaType) and call AvbSetMediaType. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbSetCrfAudioSampleClockMultiplier(dword talkerHandle, dword clockMultiplier); |  |  |  |
| Function | The function sets the audio sample clock multiplier of the CRF stream originat-ed by the Talker. Note The nominal frequency of the audio sample clock is the clock frequency (see AvbSetCrfAudioSampleClockFrequency) multiplied by the multiplier returned by this function. | Note The nominal frequency of the audio sample clock is the clock frequency (see AvbSetCrfAudioSampleClockFrequency) multiplied by the multiplier returned by this function. |  |  |
| Note The nominal frequency of the audio sample clock is the clock frequency (see AvbSetCrfAudioSampleClockFrequency) multiplied by the multiplier returned by this function. |  |  |  |  |
| Parameters | talkerHandle The handle of the Talker. |  |  |  |
| clockMultiplier The audio sample clock multiplier of the CRF stream to set. The supported values see AvbGetCrfAudioSampleClockMultiplier. |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
