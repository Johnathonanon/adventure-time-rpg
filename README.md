# Adventure Time RPG

Adventure Time RPG is a python terminal text based Role Playing Game. It is based somewhat on retro games such as 'Zork' (1977) and tabletop games like Dungeons and Dragons. In this game the user or 'player' enters a name, chooses a player class; Archer, Warrior, or Wizard, and then embarks on a short adventure through the dungeon they find themselves in. There are monsters to battle, traps to try and avoid, and rooms to make your way through, until you conquer the dungeon. The live version is deployed on heroku.

The live link can be found here - https://adventure-time-rpg.herokuapp.com/

![Picture of Excalidraw map](readme-images/excalidraw1.png) 
![Picture of AmIResponsive snip](readme-images/amiresponsivesnip.PNG) 

## How to Play

The user is initially asked to input a name and choose a class. The 3 three classes are Archer, Warrior, and Wizard. These two choices then build a player 'character'. The players choice of class dictates their 'health point' and 'attack' attributes, which are randomly generated within a range for the specific class. These are relevant when battling monsters.

![Picture of name snip](readme-images/namesnip.PNG)

![Picture of class choice snip](readme-images/classsnip.PNG)

![Picture of archer class attributes](readme-images/archersnip.PNG)
![Picture of warrior class attributes](readme-images/warriorsnip.PNG)
![Picture of wizard class attributes](readme-images/wizardsnip.PNG)

The player navigates the dungeon via a 'menu'. This menu is navigated using the arrow keys and enter key. The player has 5 choices to choose from: 
- Continue - this progresses the game to the next room if available, a short 'progress text' is printed to the terminal.
- Inspect - a brief description of the current area is printed to the terminal.
- Attack - a battle in initiated with a monster if present.
- Interact - allows the player to interact with objects if applicable.
- Flee - player flees the dungeon and ends game.

![Picture of menu snip](readme-images/menusnip.PNG)

## Features

### Existing Features

- **Player Creation**

  - User can create a 'custom' character. This includes entering a name, which defaults to 'Adventurer' if left empty, and choosing a class, with randomised stats.

  ![Picture of class choice snip](readme-images/classsnip.PNG)

  ![Picture of warrior class attributes](readme-images/warriorsnip.PNG)

- **Menu**

  - This is the main navigation tool of the game. Player has is given 5 choices:
    - Continue - this progresses the game to the next room if available, player is presented with direction choices depending on current room. Current room is then updated and a short 'progress text' is printed to the terminal. If monster presence > 0 or current room is 6 player cannot progress. If chosen direction is death room, player 'dies'.

    ![Picture of menu snip](readme-images/menusnip.PNG)

    ![Picture of direction snip](readme-images/directionsnip.PNG)

    ![Picture of no continue snip](readme-images/nocontinuesnip.PNG)

    ![Picture of death snip](readme-images/deathsnip.PNG)

    - Inspect - a brief description of the current area is printed to the terminal. Sometimes changes depending on in monster is 'dead' or 'alive'.

    ![Picture of inspect snip 1](readme-images/inspectsnip1.PNG)

    ![Picture of inspect snip 2](readme-images/inspectsnip2.PNG)

    - Attack - a battle in initiated with a monster if present. During the battle, the monster and player 'attack' each other and both their health points are reduced. If monster is defeated monster presence updates and player may continue to next room. If player is defeated game ends.

    ![Picture of battle snip 1](readme-images/battlesnip1.PNG)

    ![Picture of battle snip 2](readme-images/battlesnip2.PNG)

    ![Picture of battle snip 3](readme-images/battlesnip3.PNG)

    ![Picture of no battle snip](readme-images/nobattlesnip.PNG)

    - Interact - allows the player to interact with objects if applicable or prints a message if not. Main interactable object is portal in room 6 which 'teleports' player back to room one. This is done by updating current room value.

    ![Picture of interact snip 1](readme-images/interactsnip1.PNG)

    ![Picture of interact snip 2](readme-images/interactsnip2.PNG)

    - Flee - player flees the dungeon and ends game, a goodbye message is printed to terminal.

    ![Picture of flee snip](readme-images/fleesnip.PNG)


### Features Left to Implement

- One user stated they would like more questions or possibly a different set of questions to choose.

- I had originally intended to implement a difficulty level but chose not to. This is something I would still be interested in implementing as I feel it would only add to the enjoyability of the quiz, as well as allowing for a larger question pool, as mentioned above.

- I could possibly introduce a high score function which would store the users previous attempts and allow them to compete against themselves or others. 

## Testing

The site has been consistently tested throughout its development by both myself and others. Any time a new HTML, CSS, or JS element was introduced it was stringently tested before it was either implemented or discarded.

All html elements serve their intended purpose at time of submission. All styles work as intended and add to the overall user experience. The site has been stress tested on a large number of different browsers and screen sizes both using emulators on dev tools as well as physical mobile devices and tablets. Both myself and others viewed the site on a number of personal platforms, android and ios, and found the site to work as intended on different screen sizes and browsers.

I had some difficulty with both the checkAnswer and runQuiz functions towards the end of my project. I tried numerous different methods and spent a reasonable amount of time troubleshooting before my mentor looked at my code and offered his advice which thankfully was the push I needed to realise and rectify my mistake, which turned out to be mercifully simple. I had mistakenly written code in runQuiz which should have been in checkAnswer, and was calling checkAnswer in runQuiz instead of the other way around. Making these adjustments resulted in the code running as intended.

One user found two issues, one where he received a score of 21/20 and one where the desktop style was being applied on his android device. He states he is using the most up to date software and hardware versions and he and I are both currently unable to replicate the first issue. Below is a snip of the second, and a snip of the relevant media query on caniuse.com. He states he tried clearing cache and restarting the browser and neither had any effect, so the issue is still outstanding. 

![picture of style issue](readme-images/userscreenshot1.PNG)

![picture of caniuse.com snip](readme-images/caniusesnip.PNG)


When viewed on Microsoft Edge there are several 'issues' displayed when viewing dev tools. I brought this to the attention of my mentor as I was unable to understand the exact meaning behind them and he stated he also wasn't entirely sure on what they meant. He told me to submit as is, since the site functions as intended with no 'errors', and I would end up wasting time otherwise.

![picture of Microsoft Edge issues](readme-images/issuessnip.PNG)

Efforts were made beginning, during, and at the end of development to optimise the site as best as possible. This included colour palette generators and contrast checkers for accessibility, the addition of alt attributes where necessary, and search engine optimisation.

A colour palette was generated and the chosen colours ran through a contrast checker to ensure a pleasant experience and large degree of accessibility for the site. 

A lighthouse report was generated in order to check performance, accessibility, etc.

![picture of colour palette 1](readme-images/palettesnip1.PNG)

![picture of colour palette 2](readme-images/palettesnip2.PNG)

![another picture of contrast checker](readme-images/contrastsnip.PNG)

![picture of dev tools lighthouse snip](readme-images/lighthousesnip.PNG)

### Validator Testing

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
- JS
  - No errors were returned when passing through a JavaScript linter [JSHint](https://jshint.com/)

### Unfixed Bugs

- As mentioned above one user reported two issues which neither he nor myself were then able to replicate. I would be eager to know what caused these. 

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Main Branch
  - Once the Main Branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - https://johnathonanon.github.io/quick-quiz/

## Credits

A number of questions were found here - https://www.radiotimes.com/quizzes/pub-quiz-general-knowledge/

refreshQuiz function inspiration from here - https://stackoverflow.com/questions/5480945/refreshing-page-on-click-of-a-button/5480965

Some inspiration was taken from Code Institute lessons and the walkthrough project love-maths, specifically the implementation of the event listener on line 181 in script.js.

My mentor was very helpful and his knowledge and experience is highly appreciated. His input was especially helpful when troubleshooting the runQuiz and checkAnswer functions, on lines 116 and 160 in script.js respectively.

