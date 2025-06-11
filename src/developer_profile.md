# Developer Profile

Interactive visualistion where the user can select a country and see the distribution of developer types in that country in a stacked bar chart/waffle chart.
This should be a combination of the data visualized [here](https://survey.stackoverflow.co/2024/developer-profile#education) and [here](https://survey.stackoverflow.co/2024/developer-profile#5-geography)


```js
import { plotDeveloperProfileData } from  "./components/developer_profile.js"
const DeveloperProfileResults = FileAttachment("./data/developer_profile.json").json();
```

```js
display(DeveloperProfileResults);
```

```js
display(plotDeveloperProfileData(DeveloperProfileResults));
```