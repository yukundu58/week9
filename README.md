# Week 9

This week consists of a programming challenge designed to help
you review some of the essential ideas of the course.

You'll find a Python script, `send_weather.py`, which accomplishes the following:

1. Prompts the user for a zip code and a phone number
2. Displays the current temperature for that zip code
3. Also sends a text message to the phone number that was provided.

However:

1. Due to time constraints, it's recommended that you form a group of 2
or 3 people for this activity.
2. You will need a file named `keys.py`, not included in this repository,
in order to run the code.  This file will be posted in Canvas.  Save it
into the same folder as the `send_weather.py` file.
3. It's ok if you don't get through this entire exercise during class.
Just get as far as you can, and you can work on the remainder at home
as practice for the exam.

### The Challenge

This amazing little Python script has proved so popular across campus
that we've received a million requests to convert it into a reusable
Python module, so that other programmers can extend and build upon it!

Your job is try to to convert this script into a reusable library
that other developers can import into their own scripts.

A module named `weather.py` has been started for you already.


### Tasks

Start by _forking_ this repository, then clone your fork to your laptop.  


* Careful - do not put the `keys.py` file into your repository!

**Consider the following:**

* Are there any improvements you want to make to the current code?
* What's the best design for the module's public interface?  
* Would you prefer to drive the design with unit tests instead of trying
  to decide ahead of time?
* Are there any standard design patterns that would be helpful here?
* You must prevent actual API calls to both the weather and texting
  services while running the unit tests.

### When You Think You're Done

* Create a _pull request_ back to the original repository.  
* In your pull request description, indicate whether
you started with a design decision or if you wrote tests first in order
to drive the design.
* [Here are step-by-step instructions if you need it]( https://help.github.com/articles/creating-a-pull-request-from-a-fork/).
