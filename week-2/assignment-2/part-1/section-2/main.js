function multiplierFactory(factor) {
  let count = 0; // enclosed variable

  return {
    multiplier: function (value) {
      count++;
      return value * factor;
    },
    getCount: function () {
      return count;
    },
  };
}

function analyzeType(data) {
  if (typeof data === "number") {
    return `Number: ${data}`;
  } else if (typeof data === "string") {
    return `String: ${data}`;
  } else {
    return "Unknown Type";
  }
}

const factory = multiplierFactory(3);
console.log(factory.multiplier(5)); // 15
console.log(factory.multiplier(7)); // 21
console.log(`Function called ${factory.getCount()} times`);

const items = [10, "hello", 3.14, [1, 2]];
items.forEach((item) => {
  console.log(`Input: ${item}, Analyzed: ${analyzeType(item)}`);
});
