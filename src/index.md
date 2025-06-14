---
toc: false
---

<div class="hero">
  <h1>StackOverflow Developer Survey</h1>
  <h2>Visualizing the StackOverflow Developer Survey 2024</h2>

</div>

```js
const overview = FileAttachment("./data/overview.json").json();
```

In May 2024, over 65,000 developers responded to the annual StackOverflow survey about coding, the technologies and tools they use and want to learn, AI, and developer experience at work.

This project visualizes a selection of the survey results, focusing on the most admired and desired programming languages and the distribution of developer types per country.

<style>

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--sans-serif);
  margin: 4rem 0 8rem;
  text-wrap: balance;
  text-align: center;
}

.hero h1 {
  margin: 1rem 0;
  padding: 1rem 0;
  max-width: none;
  font-size: 14vw;
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(30deg, var(--theme-foreground-focus), currentColor);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero h2 {
  margin: 0;
  max-width: 34em;
  font-size: 20px;
  font-style: initial;
  font-weight: 500;
  line-height: 1.5;
  color: var(--theme-foreground-muted);
}

@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}

</style>
