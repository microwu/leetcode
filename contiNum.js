var a = [1, 2, 4, 5, 3, 2, 3, 3, 4, 5, 8, 10]
// if state < 0, it's increasing
// if state = 0, it's not changing
// if state > 0, it's decreasing
var state = 0
var i = 0
var sum = []
var temp = []
for (i; i < a.length - 1; i++) {
  if (state === 0) {
    temp.push(a[i])
    if (Math.abs(a[i] - a[i + 1]) === 1) {
      state = a[i] - a[i + 1]
    } else {
      sum.push(temp)
      temp = []
      state = 0
    }
  } else {
    temp.push(a[i])
    if (a[i + 1] === a[i] + (state < 0 ? 1 : -1)) {
      // do nothing
      state = a[i] - a[i + 1]
    } else {
      sum.push(temp)
      temp = []
      state = 0
    }
  }
}

if (state === 0) {
  sum.push([a[i]])
} else {
  temp.push(a[i])
  sum.push(temp)
}

console.log(sum)
