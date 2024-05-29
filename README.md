# [ARABIACHALLENGE](https://arabiachallenge-4d32641e125b.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/ibra8080/ArabiaChallenge)](https://github.com/ibra8080/ArabiaChallenge/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/ibra8080/ArabiaChallenge)](https://github.com/ibra8080/ArabiaChallenge/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/ibra8080/ArabiaChallenge)](https://github.com/ibra8080/ArabiaChallenge)



![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://arabiachallenge-4d32641e125b.herokuapp.com)
## Introduction

**ArabiaChallenge** is an engaging and educational quiz game designed to help users test and enhance their knowledge of the Arabic language. The project aims to provide a fun and interactive way for individuals to learn Arabic vocabulary and phrases, making language learning more accessible and enjoyable.

## Objectives

The primary objective of ArabiaChallenge is to:

- **Promote Language Learning**: By offering a quiz format, the project encourages users to recall and apply their knowledge of Arabic in a practical manner.
- **Enhance Vocabulary**: Each question is designed to introduce and reinforce essential Arabic words and phrases.
- **Provide Instant Feedback**: Users receive immediate feedback on their answers, allowing them to learn from their mistakes and understand the correct usage of words.

## Target Audience

ArabiaChallenge is intended for:

- **Language Learners**: Individuals who are beginning to learn Arabic or want to expand their vocabulary in an interactive way.
- **Educators and Students**: Teachers can use the game as a supplementary tool in classrooms, and students can use it for self-study.
- **Travelers and Expats**: People who are planning to visit or live in Arabic-speaking countries and want to learn basic conversational Arabic.
- **Language Enthusiasts**: Anyone with an interest in learning new languages and cultures.

## Usefulness

ArabiaChallenge is useful to its target audience in several ways:

- **Interactive Learning**: The quiz format keeps users engaged and motivated to learn more.
- **Self-paced**: Users can play the game at their own pace, allowing for flexible learning schedules.
- **Immediate Feedback**: Correct and incorrect answers are immediately identified, helping users to quickly grasp the correct terms and phrases.
- **Cultural Insight**: By learning the language, users gain insights into Arabic-speaking cultures, which can enhance their travel experiences and cultural understanding.

ArabiaChallenge combines the excitement of a quiz game with the educational benefits of language learning, making it a valuable tool for anyone looking to improve their Arabic skills in an enjoyable and effective manner.

## UX

The design of ArabiaChallenge focuses on creating an intuitive, engaging, and educational experience for users. 

### Interaction Design

1. **Simplified Navigation**: The game interface is designed to be straightforward and easy to navigate. Users can quickly start a quiz, select their answers, and receive feedback without unnecessary steps or distractions.

2. **Clear Instructions**: Each question comes with clear and concise instructions, ensuring that users understand how to interact with the quiz. The input process is streamlined to avoid confusion and maintain focus on learning.

### Feedback Mechanism

1. **Immediate Feedback**: Users receive instant feedback on their answers, helping them learn and correct mistakes in real-time. This reinforces learning and keeps users motivated.

2. **Score Tracking**: The game includes a scoring system that tracks user progress and provides a sense of accomplishment. This feature encourages users to continue playing and improving their language skills.

### Accessibility

1. **Language Support**: The game supports both Arabic and English, making it accessible to users with different language backgrounds. This bilingual approach enhances usability and learning effectiveness.

By following these design processes, ArabiaChallenge aims to provide a user-friendly and effective learning experience that caters to the diverse needs of its target audience.

## Features

### Existing Features

ArabiaChallenge offers a variety of features designed to enhance the user's learning experience. Each feature provides unique value, making the game engaging and educational for users. Below are the key features of the project, with descriptions of their value and implementation.

- ### Welcome Message

**Feature:** Welcome Message  
**Description:** The game starts with a welcoming message to greet the user.  
**Value:** Sets a friendly and inviting tone for the game, making users feel welcomed.  
**Implementation:** Implemented in the `main` function with a simple print statement.
![Welcome Message](![Final Score Display](documentation/final_score_display.png)
/welcome_message.png)

- ### Question Presentation

**Feature:** Question Presentation  
**Description:** Displays a question and multiple-choice answers to the user.  
**Value:** Provides a clear and structured format for users to read and understand the question and possible answers.  
**Implementation:** Implemented in the `get_question` function, which retrieves and prints the question and choices.
![Question Presentation](![Final Score Display](documentation/final_score_display.png)
/question_presentation.png)

- ### Arabic Text Reshaping

**Feature:** Arabic Text Reshaping  
**Description:** Corrects the display of Arabic text to be right-to-left and properly joined.  
**Value:** Ensures that Arabic text is readable and properly formatted, enhancing the user experience for Arabic speakers.  
**Implementation:** Utilizes the `arabic_reshaper` and `bidi.algorithm` libraries in the `reshape_text` function.
![Arabic Text Reshaping](![Final Score Display](documentation/final_score_display.png)
/arabic_text_reshaping.png)

- ### User Answer Input

**Feature:** User Answer Input  
**Description:** Prompts the user to enter their answer.  
**Value:** Engages the user by allowing them to participate actively in the quiz.  
**Implementation:** Implemented in the `request_answer` function, which ensures valid input through a loop and validation function.
![User Answer Input](![Final Score Display](documentation/final_score_display.png)
/user_answer_input.png)

- ### Answer Validation

**Feature:** Answer Validation  
**Description:** Validates that the user's input is one of the acceptable answers (1, 2, 3, or 4).  
**Value:** Prevents invalid inputs, ensuring that the game proceeds smoothly without errors.  
**Implementation:** Implemented in the `validate_answer` function.
![Answer Validation](![Final Score Display](documentation/final_score_display.png)
/answer_validation.png)

- ### Answer Comparison and Scoring

**Feature:** Answer Comparison and Scoring  
**Description:** Compares the user's answer to the correct answer, updates the score, and provides feedback.  
**Value:** Gives immediate feedback, helping users learn from their mistakes and rewarding correct answers with score increments.  
**Implementation:** Implemented in the `compare_answer` function, which adjusts the score and provides feedback.
![Answer Comparison and Scoring](![Final Score Display](documentation/final_score_display.png)
/answer_comparison_scoring.png)

- ### Final Score Display

**Feature:** Final Score Display  
**Description:** Displays the user's final score after all questions have been answered.  
**Value:** Provides a summary of the user's performance, giving a sense of achievement and areas for improvement.  
**Implementation:** Implemented in the `final_score` function, which prints the final score.
![Final Score Display](documentation/final_score_display.png)

#
By combining these features, ArabiaChallenge provides a comprehensive and enjoyable way for users to test and improve their Arabic language skills. Each feature has been carefully designed to contribute to an engaging and educational experience.


### Future Features

To further enhance the ArabiaChallenge experience, several future features are planned. These features aim to improve user engagement, provide additional learning resources, and create a more interactive and personalized experience.

### 1. Leaderboard

**Feature:** Leaderboard  
**Description:** Implement a leaderboard to display the top scores of users.  
**Value:** Encourages healthy competition among users, motivating them to improve their scores and engage more frequently with the quiz.  
**Implementation Plan:** Store user scores in a database and display the top scores on a leaderboard page. This feature will require user authentication to track individual progress.

### 2. Multiple Difficulty Levels

**Feature:** Multiple Difficulty Levels  
**Description:** Introduce different difficulty levels (e.g., beginner, intermediate, advanced) for the quiz questions.  
**Value:** Provides a tailored learning experience for users of varying proficiency levels, making the game more accessible and challenging for all users.  
**Implementation Plan:** Categorize questions by difficulty level and allow users to select their preferred level before starting the quiz.

### 3. Timed Challenges

**Feature:** Timed Challenges  
**Description:** Add a timed challenge mode where users must answer questions within a certain time limit.  
**Value:** Adds an element of urgency and excitement, enhancing the quiz's challenge and testing users' quick thinking and recall abilities.  
**Implementation Plan:** Implement a countdown timer for each question and adjust the scoring system to reward quick and correct answers.

### 4. Detailed Explanations

**Feature:** Detailed Explanations  
**Description:** Provide detailed explanations for each answer after the user responds.  
**Value:** Enhances learning by explaining why an answer is correct or incorrect, helping users understand the material better and retain information.  
**Implementation Plan:** Include explanations in the question data and display them after the user submits an answer.

These future features aim to make ArabiaChallenge more engaging, educational, and enjoyable, ultimately helping users improve their Arabic language skills more effectively.

## Tools & Technologies Used


- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

## Data Model

### Flowchart

To follow best practice, a flowchart was created for the app's logic,
and mapped out before coding began using a free version of
[Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning) .

Below is the flowchart of the main process of this Python program. It shows the entire cycle of the program.

![screenshot](documentation/flowchart.png)

### Classes & Functions

The ArabiaChallenge project uses various functions to modularize the code, ensuring reusability, maintainability, and clarity. Here are the primary functions used in this application:

- `reshape_text(text)`
  - Corrects the display of Arabic text to ensure it appears right-to-left and properly shaped.
- `get_question(ques_num)`
    - Retrieves and displays a question and its choices from the list of questions.
- `validate_data()`
    - Converts all string values into integers.
- `compare_answer(player_answer, correct_answer, score)`
  - Compares the user's answer with the correct answer, updates the score, and provides feedback on the user's answer.

- `final_score(total_ques, score)`
  - Displays the user's final score after all questions have been answered.

- `main()`
  - Runs the main loop of the quiz, calling other functions to display questions, collect answers, and track the score.

### Imports

I've used the following Python packages and/or external imported packages.

- `gspread`: used with the Google Sheets API
- `os`: used for adding a `clear()` function

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://arabiachallenge-4d32641e125b.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.18`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ibra8080/ArabiaChallenge) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/ibra8080/ArabiaChallenge.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ibra8080/ArabiaChallenge)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ibra8080/ArabiaChallenge)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no differences between the local version developed and the live deployment site on Heroku.

## Credits

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section you need to reference where you got your content, media, and extra help from.
It is common practice to use code from other repositories and tutorials,
however, it is important to be very specific about these sources to avoid plagiarism.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Content

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution links to any borrowed code snippets, elements, or resources.
A few examples have been provided below to give you some ideas.

Ideally, you should provide an actual link to every resource used, not just a generic link to the main site!

⚠️⚠️ EXAMPLE LINKS - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

⚠️⚠️ EXAMPLE LINKS - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution to any supports that helped, encouraged, or supported you throughout the development stages of this project.
A few examples have been provided below to give you some ideas.

⚠️⚠️ EXAMPLES ONLY - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner (John/Jane), for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.
