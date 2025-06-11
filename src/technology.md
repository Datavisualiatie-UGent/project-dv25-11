# Technology

This visualisation will be a verbatim copy of the one shown [here](https://survey.stackoverflow.co/2024/technology/#2-programming-scripting-and-markup-languages).

```js

import * as Plot from "npm:@observablehq/plot";
import { plotTechnologyData } from  "./components/technology.js"
const TechnologyResults = FileAttachment("./data/technology_results.json").json();
```

```js
display(TechnologyResults);
```

```js
display(plotTechnologyData(TechnologyResults));
```

![Stack Overflow Developer Survey 2024 - Technology](./include/stackoverflow-dev-survey-2024-technology-admired-and-desired-language-desire-admire-social.png)
