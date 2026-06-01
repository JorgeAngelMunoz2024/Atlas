
## Preference filtering 
newgrad-jobs uses a system that aggregates across multiple popular job boards, while also allowing the user to filter through multiple career paths, locations, and work models allowing for a more granular search. The idea is allowing the user to pull the links using their location and job path preferences, focusing on the following primarily:  
- Software engineering 
- Data Analyst 
- Machine Learning/AI
- Data Engineer

## Project Design 
This project will feature multiple components, the first of which will be a webscraper, that applies the desired preference filters (career path and location) and is able to first aggregate the links present to collect the different jobright listings. Once the jobright listing has been 

### API_Extractor
This will be designed with the smallest scope possible in mind, the idea behind this will be that it will execute a workflow designed below:
1. POST the `newgrad-jobs` website 
2. Enter preferences in the API request
4. With aggregated job links, extract the json files 
    - Qualification 
    - Required
    - Preferred 
    - Responsibilities
5. Utilize text found in `Qualification` as keys in dictionary, increment counter every time key is found in other sections (see above)

### K-Means Cluster Algorithm
This machine learning algorithm uses k-means algorithm to group the job lisitngs based on the ranked keywords, this will then be visualized.
1. Preprocessing - psuedo supervised classification using naive bayesian by sectioning keywords into sections of similar frameworks, languages, concepts, libraries, components.
    - Creating known sections of similarty e.g. React Related to Javascript, Typescript.
    - importing keywords from webscraper into these sections.
2. Setting the dimentsionality, clusters and iterations of the algorithm.
    - use the number of key words in the span as the dimensions and the respective popularity score of those keywords.
    - for the number of clusters we can make a guess based on the sections we create in our preclusting. 
    - The iterations will occur as every new entry from the web scraper iterating over the centroid positoning and relationships between the listing to create new sections.
3. Use 3D space to vizualize the clusters.
