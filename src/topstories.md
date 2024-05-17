---
theme: dashboard
toc: false
---

# Top stories

```js
const topstories = FileAttachment("./data/topstories.json").json();
```

```js
Inputs.table(topstories['abc'], {
  columns: [
    "Headline",
    "Rank"
  ],
  header: {
    Headline: "Headline",
    Rank: "Rank"
  }
})
```