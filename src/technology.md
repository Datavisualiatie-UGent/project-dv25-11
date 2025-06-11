# Technology

This visualisation will be a verbatim copy of the one shown [here](https://survey.stackoverflow.co/2024/technology/#2-programming-scripting-and-markup-languages).

```js
import { plotTechnologyData } from  "./components/technology.js"
const TechnologyResults = FileAttachment("./data/technology_results.json").json();
```

```js
display(TechnologyResults);
```

```js
display(plotTechnologyData(TechnologyResults));
```