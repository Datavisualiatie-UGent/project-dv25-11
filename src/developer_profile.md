# Developer Profile

## Developer Types per Country
This section provides an interactive visualization of developer types based on the StackOverflow Developer Survey 2024 data. Users can select a country to see the distribution of developer types within that country, allowing for a more detailed understanding of the developer landscape among the respondents.


The first plot shows a stacked overview of all the developer types for each country, which is not very readable because of the large number of countries. The second plot allows the user to select a country and see the distribution of developer types in that country.
```js
import { plotDeveloperProfileData, plotDeveloperProfileDataPerCountry } from  "./components/developer_profile.js"
const DeveloperProfileResults = FileAttachment("./data/developer_profile.json").json();
```

```js
// Show an overview of the developer profile data
display(plotDeveloperProfileData(DeveloperProfileResults));
```

```js

// Get the unique countries from the developer profile data
const countries = [... new Set(DeveloperProfileResults.map((d) => d.Country))];
countries.unshift("- Select a country -");

// Create a select element to choose a country
const selectCountry = html`<select>
  ${countries.map((country) => html`<option value="${country}">${country}</option>`)}
</select>`;

// Add an event listener to the select element to update the plot when a country is selected
selectCountry.onchange = (event) => {
  // Get the selected country
  const selectedCountry = event.target.value;
  display(plotDeveloperProfileDataPerCountry(DeveloperProfileResults, selectedCountry));
};

display(html`Select a country to see the distribution of developer types per country<br>`);
display(selectCountry);

```
