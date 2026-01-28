[![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi-pink.svg)](https://www.raspberrypi.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

# quill: calm, curated, connected.
_**quill**_ is your all-in-one digital information assistant on an e-paper screen. Based on the principles of 
[calm-technology](https://calmtech.com/), it aims to revive the nostalgia of a simpler time in life - information 
through periphery. <p> It's a modular system, allowing users to choose from the following pre-defined modules:
 - Cartoons (via [The New Yorker](https://www.newyorker.com/cartoons))
 - Word of the Day (via [Merriam-Webster](https://www.merriam-webster.com/word-of-the-day))
 - Artworks (via [The Maniac Scribbler](https://www.instagram.com/_themaniacscribbler_/))
 - City Calendar of Events (via [Eventbrite](https://www.eventbrite.com/d/online/all-events/))
 - News Headlines (via [News-Bulletin](https://github.com/gagansopori/News-BulletIn))

## Vision
The entire system is modular & users can choose one or more modules for their display from a set of different faces. Each 
component on the _face_ is also configurable & allows the user to override 2 configurations:
 - Update Frequency (Hourly, Daily or Weekly) or if they want to see this at a particular time (e.g.: 9 AM daily, top-of-the-hour etc.)
 - Display Time (Morning, Afternoon, Evening or Night)

## High Level Architecture 
## Hardware
Quill uses a client-server architecture, communicating using MQTT protocol. The client is a lightweight Both client & server can either be packed 
into a single device, or split into two separate devices based on user preference. 





<p>
<s>
fetches content from the internet & displays it With [RP-2040](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html) 
at its core & a vibrant e-ink display, quill aims to revive the nostalgia of the simpler things in life. You can get the 
latest news, stock market information, quotes & poems, cartoons & what not (you're only limited by your imagination & to
some extent the display driver the chip uses).

Designing an intelligent cartoon display system with user preferences involves several components. Here's a high-level 
overview of the system you might consider:
### User Authentication and Preferences:
 - Users should be able to create accounts and log in.
 - Implement a user preferences section where users can specify their interests, such as politics, sports, or other topics related to cartoons.
### Content Curation:
 - Gather a diverse set of cartoons from The New Yorker's collection. 
 - Tag each cartoon with relevant metadata, such as topics (politics, sports, music, etc.).
### Recommendation Engine:
 - Implement a recommendation engine that suggests cartoons based on the user's preferences. 
 - Use machine learning algorithms to analyze user behavior and adjust recommendations over time. 
 - Allow users to rate or provide feedback on cartoons to improve recommendations.
### Daily Calendar Feature:
 - Display a daily cartoon on the user's dashboard. 
 - Ensure that the displayed cartoon aligns with the user's preferences. 
 - Allow users to manually browse cartoons if they want to explore beyond the daily recommendation.
### Notification System:
 - Implement a notification system to remind users to check the daily cartoon. 
 - Optionally, allow users to set preferred notification times.
### User Interaction:
 - Enable users to like, share, or comment on cartoons. 
 - Provide options for users to adjust their preferences at any time.
### Responsive Design:
 - Ensure that the system is accessible and user-friendly on various devices, such as desktops, tablets, and smartphones.
### Analytics and Reporting:
 - Implement tracking mechanisms to gather data on user interactions and preferences. 
 - Use analytics to continuously improve the recommendation engine and overall user experience.
### Collaboration with The New Yorker:
 - Establish a collaboration or licensing agreement with The New Yorker to ensure the legal use of their cartoons in your system.
</s> 
</p>