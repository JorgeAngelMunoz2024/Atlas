
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

### K-Means Cluster Algorithm
This machine learning algorithm uses euclidean cluster algorithm to group the job lisitngs based on the ranked keywords, this will then be visualized.
1. Preclustering - psuedo supervised clustering by sectioning keywords into sections of similar frameworks, languages, concepts, libraries, components.
    a. Creating known sections of similarty e.g. React Related to Javascript, Typescript.
    b. importing keywords from webscraper into these sections.
2. Setting up spans of keywords and these spans will be the centroids for the job listings to cluster around. 

> ### Notes on K-Means
>>  **Questions I thought of while making these notes**
>> Would we make the depth of dimension the depths of the spans?
>> if so, we would be measureing the frequency score that is assignd to key words?
>> This question came to me because in the example below *spending score(y-axis) & Annual income (x-axis)*
>
> source:<https://reasonabledeviations.com/2019/10/02/k-means-in-cpp/?>
> kmeans clusters has 2 main tasks
> - finding groups of points in a dataset such that the total variance within groups is minimised
> - partitiohning feature space into k subsets to minimise thw within-cluster sum-of-square deviations (WCSS) which is the sum of square euclidiance disntances between each datapoint and centroid.
> the kmeans clustering problem is a complexity of O(2^n)  
>> #### (kmeans) Lloyd's algorithm, widely used time complexity of O(n\*k*id) space complexity of O(n+k)d
>> n = number of points, k = clusters, i = iterations, and d = dimensions
>> 1. Initialize the lcusters 
>> 2. Compute the centroid of each lcuster
>> 3. Assign wach to the nearest centroid and redefine the cluster
>> 4. Repeat Steps 2 and 3
> #### Issues ignored in the implementation 
> - random initialisation which results in suboptimal clusters
> - there are algorithms like k-means++ that offer mahor imporvements over k-means by specifying better procedures to find the initial clusers.
> - it actually suffers from the curse of dimensionality, as data becomes more spare in high dimensions, and it relatively inefficient since there are four loops (oover iterations, points, clusters and dimensions)