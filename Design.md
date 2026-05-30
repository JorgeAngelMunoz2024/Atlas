
## Preference filtering 
newgrad-jobs uses a system that aggregates across multiple popular job boards, while also allowing the user to filter through multiple career paths, locations, and work models allowing for a more granular search. The idea is allowing the user to pull the links using their location and job path preferences, focusing on the following primarily:  
- Software engineering 
- Data Analyst 
- Machine Learning/AI
- Data Engineer

## Project Design 
This project will feature multiple components, the first of which will be a webscraper, that applies the desired preference filters (career path and location) and is able to first aggregate the links present to collect the different jobright listings. Once the jobright listing has been 

### Web Scraper 
The webscraper will be designed with the smallest scope possible in mind, the idea behind this will be that it will execute a workflow designed below:
1. Visit the `newgrad-jobs` website 
2. Enter preferences (select field and area)
3. Aggregate job links and save somewhere
4. With aggregated job links, visit each listing and snapshot the following fields from the jobright page 
    - Qualification 
    - Required
    - Preferred 
    - Responsibilities
5. Utilize text found in `Qualification` as keys in dictionary, increment counter every time key is found in other sections (see above)
### K Means Cluster Algorithm
This machine learning algorithm uses euclidean cluster algorithm to group the job lisitngs based on the ranked keywords, this will then be visualized.
1. Preclustering - psuedo supervised clustering by sectioning keywords into sections of similar frameworks, languages, concepts, libraries, components.
    a. Creating known sections of similarty e.g. React Related to Javascript, Typescript.
    b. importing keywords from webscraper into these sections.
2. Setting up spans of keywords and these spans will be the centroids for the job listings to cluster around.