import * as Plot from "npm:@observablehq/plot";
// https://observablehq.com/@observablehq/plot-diverging-stacked-bar

function sign(type) {
  return type === "admired" ? 1 : -1;
}


export function plotTechnologyData(results) {
    return Plot.plot({
      marginTop: 30,
      marginLeft: 100,
      marginRight: 100,
      marginBottom: 30,
      x: { axis: "bottom", grid: true, tickFormat: Math.abs, label: "Count" },
      color: { scheme: "RdBu", domain: ["desired", "admired"], legend: true },
      marks: [
        Plot.barX(
          results,
          Plot.groupY(
            { x: (d) => d.length * sign(d[0].type) },
            {
              fill: "type",
              order: ["desired", "admired"],
                y: "language",
              tip: true,
            }
          )
        ),
      ],
    });
}