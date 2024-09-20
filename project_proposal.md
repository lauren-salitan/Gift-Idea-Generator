# Project Proposal

Use this template to help get you started right away! Once the proposal is complete, please let your mentor know that this is ready to be reviewed.

The Gift Idea Generator is a web-based application designed to revolutionize the gift-giving experience by providing personalized gift suggestions. Utilizing Python, Flask, PostgreSQL, and a suite of front-end technologies, this app allows users to create accounts, wherein they can generate, save, and revisit recipient profiles and past searches. By filling out a detailed questionnaire about the gift recipient's interests, occasions, and preferences, users receive AI-driven recommendations, possibly enhanced by integrating external APIs like OpenAI for generating ideas and shopping APIs for product availability. This tool aims to simplify the decision-making process in selecting gifts, making it both user-friendly and highly personalized for each unique recipient, thereby catering to a wide demographic of users looking to enhance their gift-giving with thoughtful, tailored suggestions.

## Get Started

|       | Description | Fill in |
| ----- | ----------- | ------- |

| Tech Stack | The project will utilize Python/Flask for the backend, PostgreSQL and SQLAlchemy for database management, Heroku for deployment, Jinja for templating, and JavaScript, HTML, CSS for the frontend. RESTful APIs will be integrated for external data fetching. WTForms will be used for form handling and validations. | Python/Flask, PostgreSQL, SQLAlchemy, Heroku, Jinja, RESTful APIs, JavaScript, HTML, CSS, WTForms |

| Type | This will be a web-based application accessible via browsers on both desktop and mobile devices. | Web Application |

| Goal | The project aims to simplify the process of finding personalized gift ideas through a user-friendly interface that leverages AI to generate suggestions based on recipient profiles. | Simplify gift finding with AI-driven suggestions |

| Users | The app will cater to individuals looking for gift ideas for friends, family, or colleagues. This includes users of all ages who are comfortable with basic web navigation and input forms. | General web users seeking gift ideas |

| Data | Data will be collected through user inputs in forms creating recipient profiles. External data might be fetched using RESTful APIs like OpenAI for generating ideas and possibly Amazon or Google Shopping APIs for product searches. In addition to user-generated profiles, the database will  also store user login information and records of past searches and saved recipients. This ensures that users can return to their previous ideas and add or modify recipient profiles as needed.Users can create and manage their own recipient profiles in the system.| User-generated profiles, External product APIs |

# Breaking down your project

When planning your project, break down your project into smaller tasks, knowing that you may not know everything in advance and that these details might change later. Some common tasks might include:

- Determining the database schema
- Sourcing your data
- Determining user flow(s)
- Setting up the backend and database
- Setting up the frontend
- What functionality will your app include?
  - User login and sign up
  - Uploading a user profile picture

Here are a few examples to get you started with. During the proposal stage, you just need to create the tasks. Description and details can be edited at a later time. In addition, more tasks can be added in at a later time.

|Task Name| Description| Example|
| ------- | ---------- | ------ |
<!-- 
| Design Database schema| Determine the models and database schema required for your project.                                           | [Link](https://github.com/hatchways/sb-capstone-example/issues/1) |
| Source Your Data| Determine where your data will come from. You may choose to use an existing API or create your own.           | [Link](https://github.com/hatchways/sb-capstone-example/issues/2) |
| User Flows| Determine user flow(s) - think about what you want a user’s experience to be like as they navigate your site. | [Link](https://github.com/hatchways/sb-capstone-example/issues/3) |
| Set up backend and database | Configure the environmental variables on your framework of choice for development and set up database.| [Link](https://github.com/hatchways/sb-capstone-example/issues/4) |
| Set up frontend | Set up frontend framework of choice and link it to the backend with a simple API call for example.            | [Link](https://github.com/hatchways/sb-capstone-example/issues/5) |
| User Authentication| Fullstack feature - ability to authenticate (login and sign up) as a user                                     | [Link](https://github.com/hatchways/sb-capstone-example/issues/6) | -->
|Design Database schema| Determine the models and database schema needed to store user and recipient profile information, as well as gift ideas.| [Link](https://github.com/hatchways/sb-capstone-example/issues/1)|

| Source Your Data| Identify and integrate external APIs like OpenAI for gift suggestions and shopping APIs for product searches.| [Link](https://github.com/hatchways/sb-capstone-example/issues/2) |

| User Flows| Outline the user experience from registration to receiving gift suggestions, including all intermediary steps.| [Link](https://github.com/hatchways/sb-capstone-example/issues/3) |

| Set up backend and database | Configure Flask environment, set up PostgreSQL database, and integrate with SQLAlchemy.| [Link](https://github.com/hatchways/sb-capstone-example/issues/4) |

| Set up frontend| Develop the frontend using HTML, CSS, and JavaScript. Connect it to the backend through AJAX calls for dynamic content.| [Link](https://github.com/hatchways/sb-capstone-example/issues/5) |

| User Authentication | Create functionality for user registration, login, and session management to ensure users can securely access and manage their own information. Implement user authentication to enable personalization and secure management of recipient profiles.| [Link](https://github.com/hatchways/sb-capstone-example/issues/6) |

| Develop User Profile Management | Allow users to create, modify, and delete recipient profiles and view their past searches. This task will involve both frontend and backend development to handle the data.|

|Implement Data Persistence for Saved Searches | Develop functionality to save and retrieve users' past searches for gift ideas. This includes adjustments to the database schema to accommodate storing search parameters and results.|


## Labeling

Labeling is a great way to separate out your tasks and to track progress. Here’s an [example](https://github.com/hatchways/sb-capstone-example/issues) of a list of issues that have labels associated.


| Label Type| Description| Example|
| --------- |------------| -------|
<!-- 
| Difficulty | Estimating the difficulty level will be helpful to determine if the project is unique and ready to be showcased as part of your portfolio - having a mix of task difficultlies will be essential.| Easy, Medium, Hard|

| Type| If a frontend/backend task is large at scale (for example: more than 100 additional lines or changes), it might be a good idea to separate these tasks out into their own individual task. If a feature is smaller at scale (not more than 10 files changed), labeling it as fullstack would be suitable to review all at once. | Frontend, Backend, Fullstack |

| Stretch Goals | You can also label certain tasks as stretch goals - as a nice to have, but not mandatory for completing this project.| Must Have, Stretch Goal| 
 -->

| Difficulty | Tasks will be categorized by complexity to balance workload and ensure a comprehensive demonstration of skills.| Easy, Medium, Hard|

| Type| Tasks will be distinguished between frontend, backend, and full-stack based on the scope of the changes required. | Frontend, Backend, Fullstack |

| Stretch Goals | Additional features like integration with Google Maps API for geolocation-based suggestions will be considered as stretch goals.| Must Have, Stretch Goal| 

| Priority | Some tasks are critical for the basic functionality of the app (like user authentication), while others may enhance user experience but are not crucial for the initial launch (like saving searches) | Essential, Optional |