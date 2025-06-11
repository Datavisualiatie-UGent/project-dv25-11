# Technology

## Admired and Desired Programming Languages
This section visualizes the most admired and desired programming languages based on the StackOverflow Developer Survey 2024 data. The data is presented in a diverging stacked bar chart format, where the left side shows the most desired languages and the right side shows the most admired languages.

```js
import { plotTechnologyData } from  "./components/technology.js"
const TechnologyResults = FileAttachment("./data/technology_results.json").json();
```

```js
display(plotTechnologyData(TechnologyResults));
```