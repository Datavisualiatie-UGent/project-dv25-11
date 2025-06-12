import * as Plot from "npm:@observablehq/plot";

export function plotDeveloperProfileData(results) {
    return Plot.plot({
      grid: true,
      marginBottom: 175,
      marginRight: 100,
      width: window.innerWidth,
      height: window.innerHeight,
      fx: {
          tickRotate: 90,
      },
      marks: [
        Plot.waffleY(
          results,
          Plot.groupZ(
            { y: "count" },
            {
              fill: "DevType",
              y: "count",
              fx: "Country",
              tip: true,
              unit: 50,
            }
            ),
        ),
      ],
    });
}

export function plotDeveloperProfileDataPerCountry(results, country) {
  results = results.filter((d) => d.Country === country);
  return Plot.plot({
    grid: true,
    marginLeft: 200,
    width: window.innerWidth,
    height: window.innerHeight,
    y: {
      // Remove the 'developer' prefix from the x-axis labels
      tickFormat: (d) => d.replace(/Developer, /g, " "),
    },
    marks: [
      Plot.barX(
        results,
        Plot.groupY(
          { x: "count" },
          {
            y: "DevType",
            fill: "DevType",
          }
        )
      ),
    ],
  });
}