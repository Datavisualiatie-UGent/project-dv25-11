# Developer Profile

Interactive visualistion where the user can select a country and see the distribution of developer types in that country in a stacked bar chart/waffle chart.
This should be a combination of the data visualized [here](https://survey.stackoverflow.co/2024/developer-profile#education) and [here](https://survey.stackoverflow.co/2024/developer-profile#5-geography)


## Needs
- `country` field
- `DevType` field
- custom `count` field
- custom `total` field

```js
const DeveloperProfileResults = FileAttachment("./data/developer_profile.json").json();
```

```js
display(DeveloperProfileResults);
```

```js
let total = DeveloperProfileResults.length;

function countUniqueDevTypes(inputArray) {
  const uniqueCounts = {};
  const result = [];

  for (const item of inputArray) {
    const key = `${item.country} - ${item.DevType}`;
    if (uniqueCounts[key]) {
      uniqueCounts[key].count++;
    } else {
      uniqueCounts[key] = { country: item.country, DevType: item.DevType, count: 1 };
    }
  }

  for (const key in uniqueCounts) {
    result.push(uniqueCounts[key]);
  }

  return result;
}

let count = countUniqueDevTypes(DeveloperProfileResults);


display(count);
```

```js
Plot.plot(
    marks: [
        Plot.waffleY(
            count,
            Plot.groupX(
                {x: "country", y: "DevType"},
                {y: "count", fill: "DevType"}
            )
        )
    ]
)


```