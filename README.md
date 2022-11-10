# Python (Back-end)
The back end and data collection of this project is run using Python along with the selenium library.  It collects data from Wikipedia's page view API to check each celebrity's "popularity" or "relevance" by checking each celebrity's page views over a specific time period.  In addition, it scrapes height data from https://www.celebheights.com/, as they have the best readily available database of celebrity heights.  Finally, it collects net worth data from https://www.celebritynetworth.com, as they have the best readily available database of celebrity net worths.  It then creates an entry in a json file, to be handed off the front end of this project.

A different module of the Back-end uses the icrawler library to fetch images for each celebrity in the generated data set.

# HTML, JS, CSS (Front-end)
The front end uses a culmination of the web suite to dynamically create a list of celebrities that are shorten or equal in height than the user's inputted height.  It uses a variety of custom made methods to filter the celebrities (to people shorter) and sort the celebrities by the user's desired paramters (by popularity, net worth, height or name).

# What I Learned
Although this is a random and very niche project, I took it up to gain experience with both Back-end and Front-end programming, and working on a project that has direct interaction between the two.  I'm extremely happy with the entire execution of this project and the code I created to make it work.  It was a really intelectually demanding project but I'm glad that I was able to build something that I'm really proud of.
