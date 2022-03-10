const Koa = require('koa')
const fs = require('fs')

const PORT = 43191

const app = new Koa


app.use(function (ctx) {
  ctx.set('content-type', 'text/html')
  ctx.body = fs.readFileSync('./index.html')
})



app.listen(PORT, () => {
  console.log(`http://localhost:${PORT}`)
})