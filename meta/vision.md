# Vision
My aim is to create a larger game than Civilization, featuring more civilizations. This might not be possible due to engine limitations (I'll discuss this in more depth in the "Being Realistic" section), but I'm willing to sacrifice visual complexity for increased size and gameplay complexity.

I want to develop a game more complex than Civ6, while retaining its core gameplay, which I find fun and engaging. However, Civ6 requires mods for added complexity, which can cause engine issues. The game has limited systems and lacks the flexibility to extend those systems easily. Therefore, I plan to design the code with numerous callback options, allowing mods to dynamically register with core systems and even control core manager objects to influence the game. This might introduce security risks, especially with mods and online play, due to the dynamic nature of the code, which could define instances of random saveable objects.

Goals I would like to achieve include:

- A more modern event system to guide players through events with consequences and goals.
- Diverse playstyles.
- Longer, more complex games.
- Larger maps.
- Enhanced city and citizen management, which is basic in Civ and could be deepened.
- More resources, with scalability. I believe it's fun to have various bonus resources available.
- Better mod-ability from the core up.
- Multiplayer (a future consideration).
- A viable World Congress.
- Interesting victory conditions for different playstyles.
- More intriguing routes, such as full corporate, anarchist, or full union, similar to a Stellaris-style approach.

## Being Realistic

 As a solo developer working on a side project, this might just end up as an interesting experiment I eventually set aside. However, I love Civilization and feel Firaxis is heading in the wrong direction. I believe Civ5 was the peak, but Civ6 still has some great ideas.

I am primarily a backend developer with no prior experience in game development or game GUIs, which is quite intimidating, but I will figure it out. I might need to switch engines or drop down to Panda3D's core to start working, as I have some doubts about the current engine. If needed, I can fork the engine since it's built on top of Panda3D.

I understand this will be a significant amount of work, having already set up and created a few systems. Nevertheless, I have the time and no deadlines.

## Technical Limitations

As far as I can envision and have tested, if I keep most of the logic outside of rendering objects, the engine should remain light and fast while handling game logic, possibly even asynchronously to improve performance. This approach reduces the load on the engine by limiting the objects it needs to manage.

If performance becomes an issue, we might need to resort to lower-level languages, such as using a C extension for core math operations and some engine tasks. However, given current hardware capabilities, I believe I can achieve sufficient performance to make the game accessible to a wide audience.

The main limitation at this point is my inexperience in game development and my limited skills in vector and 3D math, as well as modeling and UI design. However, I believe I can figure these out within an acceptable timeframe to an acceptable manner that would allow me to finish a basic version and these things can always be improved later aslong as the core game logic is sound.
