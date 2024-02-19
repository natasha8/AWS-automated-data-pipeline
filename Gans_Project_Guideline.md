##Introduction 

Some of Gans’ most notorious and well-established competitors are TIER, probably the biggest player in the German-speaking countries, now expanding throughout other European countries, and Bird, a cool Californian company, already established in Europe.

The focus of most e-scooter companies is sustainable mobility: they are on the good side of the dichotomy between Battery Electric Vehicles (BEV) versus Internal Combustion Engine Vehicles (ICEV). Most of their marketing efforts push the eco-friendly narrative: this is how they acquire new users and gain good press from citizens encountering scooters around the city.

However, Gans has seen that its operational success depends on something more mundane: having its scooters parked where users need them.

Ideally, scooters get rearranged organically by having certain users moving from point A to point B, and then an even number of users moving from point B to point A. However, some elements create asymmetries. Here are some of them:

In hilly cities, users tend to use scooters to go uphill and then walk downhill.
In the morning, there is a general movement from residential neighbourhoods towards the city centre.
Whenever it starts raining, e-scooter usage decreases drastically.
Young tourists travelling with cheap flights are a big potential group of users, but they need to find scooters downtown or nearby touristic landmarks.
There are some actions that the company can perform to solve these asymmetries, namely:

Use a truck to move scooters around.
Create economic incentives for users to pick up or leave scooters in certain areas.

Either way, the company wants to anticipate as much as possible scooter movements. Predictive modelling is certainly on the roadmap, but the first step is to collect more data, transform it and store it appropriately. 


---------

Task: collect data from external sources that can potentially help Gans predict e-scooter movement. Since data is needed every day, in real-time and accessible by everyone in the company, the challenge is going to be to assemble and automate a data pipeline in the cloud.

### Create an automated data pipeline
 
 
#### Phase 1: Local pipeline
    In this first phase you will run scripts to collect data from the internet and store the data in a database. The scripts will be executed    by your computer, in Jupyter notebooks, and the database will also be created in your local MySQL instance —also on your own computer.

    1.1. Scrape data from the web
    Some of the data you will need is going to be floating around the internet, as the content of websites. You will have to learn how to access this information by downloading and extracting the HTML code of these sites, mostly using Python’s most popular web scraping library: beautifulsoup.

    1.2. Collect data with APIs
    The internet is full of data providers. To acquire the specific data you need, you will need to learn how to authenticate yourself and assemble a request with the right parameters. All of this is done through little pieces of software called APIs. Python’s requests library is going to be your main tool to interact with APIs.

    1.3. Create a database model
    When you collect data with Python scripts, you will have data stored as dictionaries or Pandas DataFrames. Python objects are great for local exploration and analysis, but not the best format to make data quickly available to the rest of the company. Relational databases are the solution.

    Determining the logical structure of the database is an important first step when a company wants to start storing data in a relational database. Which tables will you need? How will these tables be related to each other? Only after answering these questions (and more), you will create the database.

    1.4. Store data on a local MySQL instance
Once you’ve created the database model, you will test that the connection between Python and MySQL works by setting up the database locally on your computer and storing the data you collected from the APIs and your web scraper on it.


#### Phase 2: Cloud Pipeline
If you use Google Drive or Apple’s iCloud, your files are already on the cloud. The cloud is a catch-all name for any technological resources or services accessed via the internet. And it has many advantages when it comes to building data pipelines: scalability, flexibility, automation, maintenance…

    2.1. Set up a cloud database
    The first step in moving your pipeline to the cloud will be the storage one. You will use RDS, the Relational Database Service from the largest public cloud provider: Amazon Web Services (AWS), to set up your MySQL database.

    2.2. Move your scripts to Lambda
    Lambda is an AWS service for running code seamlessly in the cloud. You will move your data collection scripts from Jupyter Notebooks into AWS Lambda functions.

    2.3. Automate the pipeline
    One of the advantages of running code in AWS is that scheduling and automation are easy. In our case, we will use CloudWatch Events / EventBridge to create rules that will trigger the execution of the data collection scripts.
    
    
    
#### Embrace iteration
    Data pipelines can get more complex than that. It’s important to limit the scope of this project:

    We will not connect our data pipeline to a BI tool.
    We will not be creating either a data warehouse or a data lake.
    We will not work with big data, data streaming or parallel computing.
    And this is how it should be! All tech projects start with a simple approach before moving on to cool (but oftentimes, complicated) solutions.

    This is also the reason why we will first build the pipeline locally and, only once it’s done, we will move to the cloud: we anticipate we will make mistakes, identify needs we were not foreseeing and come up with new ideas along the way. We want all of this to happen as early as possible and in a context where debugging code or altering the design of a database is still easy.
    
#### Prepare your deliverable
The deliverable of this project is a written description of what you have accomplished: A Medium article.

Medium is a collaborative blogging platform where a lot of individuals from the technical and business world share their thoughts and experiences. Anyone can write a post, and if it generates a good amount of views and catches the eye of an editor, it might even get featured in a specialised Medium sub-platform such as Towards Data Science.

It’s a great idea to start drafting the article as you go through the project: note down the problems you encounter and how you overcome them, the resources that help you the most and the learnings you make along the way. You will appreciate it by the end of the project when you have to finalize your writing.

    



 



