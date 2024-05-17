---
theme: dashboard
toc: false
pager: false
---

```js
let date = new Date();
let eastCoastTime = date.toLocaleString('en-US', {   hour: "numeric",
  minute: "2-digit", month:"short", day:"numeric", timeZone: 'Australia/Melbourne'});
```

# Top stories
Last updated ${eastCoastTime}


```js
const topstories = FileAttachment("./data/topstories.json").json();
```

```js
function tableau(source, key){
  return Inputs.table(source[key], {
  columns: [
    "Headline",
    "Rank"
  ],
  header: {
    Headline: "Headline",
    Rank: "Rank"
  }
})
}
```

<div class="grid grid-cols-2">
  <div class="card" style="padding: 0;">
      <h2>ABC</h2>
    ${tableau(topstories, 'abc')}

  </div>
    <div class="card" style="padding: 0;">
    <h2>Google top stories</h2>
    ${tableau(topstories, 'google_top')}
  </div>
</div>

<div class="grid grid-cols-2">
  <div class="card" style="padding: 0;">
      <h2>Guardian Australia</h2>
    ${tableau(topstories, "graun")}

  </div>
    <div class="card" style="padding: 0;">
    <h2>SMH</h2>
    ${tableau(topstories, "smh")}
  </div>
</div>