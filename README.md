# crowdfunding_back_end
FitFlare By Sahar

## Planning:
### Concept/Name

This health and fitness crowdfunding site allows people to ask for sponsership for a variety of innovations, spanning wearable devices, smart fitness equipment, nutritional supplements, wellness apps, and more. This project aim to enhance well-being, physical activity, and overall health. Common elements include wearable devices, smart fitness equipment, Nutritional Supplement, Health Apps and Software, Health Monitoring Devices, Personalized Health Services, education programs and workshops, Community Wellness Projects and etc.

### Intended Audience/User Stories

The intended audience for this health and fitness-related crowdfunding site may vary based on the specific product or project. However, in general, the target audience typically includes individuals who have an interest in maintaining a healthy lifestyle, improving their fitness, and exploring innovative health and wellness solutions. 
Some example of the primary target audiences for this project :​

Health and Fitness Enthusiasts: who are eager on maintaining a healthy lifestyle.​
Technology Enthusiasts: Those interested in the latest health tech innovations.​
Wellness Consumers: People prioritizing overall well-being.​
Health Professionals: Healthcare, fitness, and nutrition experts seeking new tools.​
Outdoor Enthusiasts: Those interested in outdoor fitness and adventure.​
Mental Health Advocates: Individuals concerned about mental well-being.​
Cooking and Nutrition Enthusiasts: Passionate about healthy eating and kitchen innovations.​
Fitness Gamers and VR Fans: Gamers and tech enthusiasts interested in interactive fitness experiences.

### Front End Pages/Functionality
- Home page:
- Navigation bar
- Login form
- Categories to help users navigate.
- Overview of featured and popular projects.

- Project Listing Page:
- Displays a grid or list of projects.
- Project cards with images, titles, brief descriptions, and funding progress.

- Project Details Page:
- In-depth information about a specific project.
- Project description, goals, and timeline.
- Funding progress bar.
- Options to share on social media.
- List of supporters and their contributions.

- User Registration and Login:
- Registration and login forms.

- Create Project Page:
- Form for project creators to submit their project details.
- Fields for project Title, name, goal amount, status, description and date created.
- Upload images and videos to showcase the project.
- Pledge form:
- A form that will allow a logged in user to support a project.
- Brief detail about the project being supported, comments, amount and the option for supporter to stay anonymous.

- 404 Error Page:
- Custom 404 error page for a better user experience.

### Screenshots

GET Method
![]( {{ ./relative/path/to/your/schema/image.png }} )

POST Method
![]( {{ ./relative/path/to/your/schema/image.png }} )

Token Feature
![]( {{ ./relative/path/to/your/schema/image.png }} )

### API Spec
| URL | HTTP Method | Purpose | Authentication/ Authorisation  | Implemented Yet |
| /projects/ | POST | Project object (without id or date_created)| Must be logged in | YES|
|     |             |         |         |              |                       ||


### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )