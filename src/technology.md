# Technology

## Admired and Desired Programming Languages
This section visualizes the most admired and desired programming languages based on the StackOverflow Developer Survey 2024 data. The data is presented in a diverging stacked bar chart format, where the left side shows the most desired languages and the right side shows the most admired languages.

```js
import { plotTechnologyData, plotTechnologyDataPerDevType } from  "./components/technology.js"
const TechnologyResults = FileAttachment("./data/technology_results.json").json();
```

```js
display(plotTechnologyData(TechnologyResults));
```

The following plot allows to select a specific programming language to see its distribution across different developer types. This provides insights into how various programming languages are perceived and utilized by different segments of the developer community.

```js
// Get the unique programming languages from the technology data
const languages = [... new Set(TechnologyResults.map((d) => d.language))];
languages.unshift("- Select a language -");

// Create a select element to choose a programming language
const selectLanguage = html`<select>
  ${languages.map((language) => html`<option value="${language}">${language}</option>`)}
</select>`;
display(selectLanguage);

// Add an event listener to the select element to update the plot when a country is selected
selectLanguage.onchange = (event) => {
  // Get the selected country
  const selectedLanguage = event.target.value;
  display(plotTechnologyDataPerDevType(TechnologyResults, selectedLanguage));
};
```
