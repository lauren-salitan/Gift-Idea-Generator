# Project Ideas

In this file (but not restricted to), you can use to get used to working on this repository and jot down project ideas to easily be shared with your mentors and to keep the history of!

Idea #1:
Gift idea generator
    - User creates a gift recipient, fill out a form to describe the person they are wanting to give a gift to
    - Uses the openAI api to generate gift ideas based on the recipient description, then a search for those products takes place


Idea #2:
Running shoe product identification form/quiz
    - User takes quiz (product identification form) to identify best running shoe type, without user needing to have any knowledge about shoe specifications
    - Shoe class, with properties such as gender(), heel drop (integer), cushioning (), running type (trail or road), running style (long runs, racing, daily trainers, etc.), toe box (), special conditions()
    - Questions would be translated
        - i.e. to figure out what heel drop the shoes should have, rather than asking "what heel drop would you prefer?", asking something like "do you tend to strike with your heel, midfoot, or forefoot?" translating someone saying heel strike to higher drop, for example
    - Upon finishing, either:
        - A. connecting to the amazon shopping API and searching based on results
        or
        - B. having a database of options, doing a query to find a match, then searching based on that

Idea #3:
Digital Jukebox
    - A vendor (restaurant/bar/club) can have a little QR code where customers can use a digital jukebox
    - Similar to Mr.Yum, where you can scan to order off a menu, but instead you scan to request a song to be played
    - Connects to the spotify api, builds a playlist with a queue
    <!-- - Vendors have the option whether or not to charge people to add a song
    - Vendors can either 1. have a set playlist where any song on that list can be played, but only songs on that list, 2. let it be any song off of Spotify, or 3. Any song on Spotify can be requested, but requires admin approval
    - Customers can pay to ‘bump’ their song up a queue, upvote/downvote a song -->