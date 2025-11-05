# Nari_app
🤖 NariApp: Automated Emergency Response System

NariApp: Automated Emergency Response System. 🛡️ Utilizes voice detection and an SOS button to capture real-time photo/audio evidence, instantly notifying parents via a dedicated application.

✨ Project Overview: NariApp

NariApp is an advanced personal safety solution built for modern family security. Its core architecture is designed to minimize response time in critical situations through two-way activation and rich data capture.

This system leverages on-device sensors to automatically activate SOS when a user's voice indicates distress. Alternatively, it can be triggered instantly via a physical button press. Upon activation, the application covertly engages the camera and microphone, securing vital, real-time context and evidence that is immediately pushed to a connected parent application.

⚙️ Core Technical Features

Feature	Mechanism & Value Proposition
Automated Voice SOS	Utilizes speech-to-text and keyword detection to automatically trigger an alert when a user is heard speaking emergency-related phrases, enabling hands-free operation in a crisis.
Dual-Mode Activation	Supports both the high-reliability, one-touch SOS button and the innovative, automatic voice trigger to ensure an alert is sent no matter the situation.
Real-Time Media Pipeline	Immediately and discreetly captures a photo and audio clip from the user's environment, providing verifiable context and evidence to emergency contacts.
Dedicated Notification Bridge	Ensures reliable, instant delivery of the alert, media, and precise GPS location data to the linked Parent/Guardian application via a secure notification service.
Event Logging & Persistence	(Assuming you fix the sqlite3 issue) Securely logs all SOS events, location data, and communication statuses within a local database for post-event analysis and reliability auditing.


