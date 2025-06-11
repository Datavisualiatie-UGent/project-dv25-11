# project-dv25-11 Progress Report

All work was performed by [Matthias De Smet](@matthdsm)

## Data acquisition

The data was acquired from the [StackOverflow Developer Survey 2024](https://survey.stackoverflow.co/datasets/stack-overflow-developer-survey-2024.zip) and is available in the `src/data` directory as a compressed CSV file.

## Data loaders

I used a simple python script to extract the relavant columns from the CSV file and export to JSON format, which is then used in the visualizations.
Data is loaded using the `FileAttachment` API from Observable.


## Visualizations

We load the data for each visualiation separately on page load. This does increase the network traffic but allows us to keep the visualizations modular and independent of each other. Since the entirety of the dataset is quite large,  I think this trade-off is acceptable.

### Technology plot
The `technology` plot is meant to be a simpler copy of the one shown below:

<img src="src/include/stackoverflow-dev-survey-2024-technology-admired-and-desired-language-desire-admire-social.png" width="600">


The point is to visualize a list of the most admired and desired programming languages.
To simplify the visualization, I will use the absolute count of answers, rather than a percentage and show the data as a diverging stacked bar chart, where the left side shows the most desired languages and the right side shows the most admired languages, as shown in the example below:

![Technology attempt 1](src/include/technology-attempt1.png)


Further iterations should include a functional tooltip with relevant information and a more polished design. I should also consider reverting to showing percentages to give a better overview of the data.
Furthermore it would be useful to include the respondent `developer type` and allow a selectable filter to show the data for a specific developer type.
